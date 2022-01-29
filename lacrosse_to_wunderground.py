import sys
import time
import requests
import json
import datetime

email = "La Crosse View Account Email"
password = "La Crosse View Password"
station_id = "WU PWS ID"
station_key = "WU PWS Key"
api_key = "WU Account API Key"
device_name_auctual = "the name of the device you want to query"


def lacrosse_login(email, password):
    url = (
        "https://www.googleapis.com/"
        "identitytoolkit/v3/relyingparty/verifyPassword?"
        "key=AIzaSyD-Uo0hkRIeDYJhyyIg-TvAv8HhExARIO4"
    )
    payload = {"email": email, "returnSecureToken": True, "password": password}
    r = requests.post(url, data=json.dumps(payload))
    body = r.json()
    token = body.get("idToken")

    if token is None:
        raise ConnectionError("Login Failed. Check credentials and try again")
    return token


def lacrosse_get_locations(token):
    url = (
        "https://lax-gateway.appspot.com/"
        "_ah/api/lacrosseClient/v1.1/active-user/locations"
    )
    headers = {"Authorization": "Bearer " + token}
    r = requests.get(url, headers=headers)
    if r.status_code < 200 or r.status_code >= 300:
        raise ConnectionError("failed to get locations ()".format(r.status_code))
    body = r.json()
    return body.get("items")


def lacrosse_get_devices(token, locations):
    devices = list()
    for location in locations:
        url = (
            "https://lax-gateway.appspot.com/"
            "_ah/api/lacrosseClient/v1.1/active-user/location/"
            + location["id"]
            + "/sensorAssociations?prettyPrint=false"
        )
        headers = {"Authorization": "Bearer " + token}
        r = requests.get(url, headers=headers)
        if r.status_code < 200 or r.status_code >= 300:
            raise ConnectionError(
                "failed to get weather data error: {}".format(r.status_code)
            )
        body = r.json()
        if body:
            raw_devices = body.get("items")
            for device in raw_devices:
                sensor = device.get("sensor", {})
                devices.append(
                    {
                        "device_name": device.get("name").lower().replace(" ", "_"),
                        "device_id": device.get("id"),
                        "sensor_type_name": sensor.get("type", {}).get("name"),
                        "sensor_id": sensor.get("id"),
                        "sensor_field_names": [
                            x
                            for x in sensor.get("fields")
                            if x.lower() != "notsupported"
                        ],
                        "location": location,
                    }
                )
    return devices


def lacrosse_get_weather_data(token, device, time_zone="America/New_York"):
    fields_str = (
        ",".join(device["sensor_field_names"]) if device["sensor_field_names"] else None
    )

    aggregates = "ai.ticks.1"
    start = "from=" + str(int(time.time() - 43200))
    end = "to="

    url = (
        "https://ingv2.lacrossetechnology.com/"
        "api/v1.1/active-user/device-association/ref.user-device.{id}/"
        "feed?fields={fields}&"
        "tz={tz}&"
        "{_from}&"
        "{to}&"
        "aggregates={agg}&"
        "types=spot".format(
            id=device["device_id"],
            fields=fields_str,
            tz=time_zone,
            _from=start,
            to=end,
            agg=aggregates,
        )
    )

    headers = {"Authorization": "Bearer " + token}
    r = requests.get(url, headers=headers)
    if r.status_code < 200 or r.status_code >= 300:
        raise ConnectionError(
            "failed to get weather data error: {}".format(r.status_code)
        )
    body = r.json()
    return (
        body.get("ref.user-device." + device["device_id"])
        .get("ai.ticks.1")
        .get("fields")
    )


def wunderground_upload_data_point(
    station_id, station_key, weather_data, utc_timestamp
):
    payload = {
        "action": "updateraw",
        # 'dateutc': 'now',
        "dateutc": timestamp_format(utc_timestamp),
        "ID": station_id,
        "PASSWORD": station_key,
        "realtime": 1,
        "rtfreq": 2.5,
    }
    payload.update(weather_data)
    try:
        requests.get(
            "http://rtupdate.wunderground.com/weatherstation/updateweatherstation.php",
            params=payload,
        )
    except Exception:
        print("Failed to post weather update to wunderground.")


def timestamp_format(utc_timestamp):
    return datetime.datetime.utcfromtimestamp(utc_timestamp).strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def wunderground_get_utc_of_latest(station_id, api_key):
    try:
        r = requests.request(
            "GET",
            "https://api.weather.com/v2/pws/observations/current?stationId="
            + station_id
            + "&format=json&units=e&apiKey="
            + api_key,
        )
        j = json.loads(r.content.decode("utf-8"))
        ts = datetime.datetime.strptime(
            j["observations"][0]["obsTimeUtc"], "%Y-%m-%dT%H:%M:%S%z"
        ).timestamp()
    except Exception:
        ts = int(time.time() - 300)
        print("Warning: Didn't get latest observation time, loading last 5 min")
    return int(ts)


def celsius_to_fahrenheit(celsius):
    return (celsius * (9 / 5)) + 32


def kilometers_per_hour_to_miles_per_hour(kilometers_per_hour):
    return kilometers_per_hour / 1.609


def push_all_since_timestamp_to_wunderground(w, old_utc_timestamp):
    for temp_data, humidity_data, wind_data, WindHeading in zip(
        w["Temperature"]["values"],
        w["Humidity"]["values"],
        w["WindSpeed"]["values"],
        w["WindHeading"]["values"],
    ):
        utc_timestamp = temp_data["u"]
        if utc_timestamp > old_utc_timestamp:
            weather_data = dict(
                tempf=celsius_to_fahrenheit(temp_data["s"]),
                humidity=humidity_data["s"],
                windspeedmph=kilometers_per_hour_to_miles_per_hour(wind_data["s"]),
                winddir=WindHeading["s"],
            )
            wunderground_upload_data_point(
                station_id, station_key, weather_data, utc_timestamp
            )
            # time.sleep(2.5)


if __name__ == "__main__":
    try:
        old_utc_timestamp = int(sys.argv[1])
    except Exception:
        old_utc_timestamp = wunderground_get_utc_of_latest(station_id, api_key)
    token = lacrosse_login(email, password)
    locations = lacrosse_get_locations(token)
    devices = lacrosse_get_devices(token, locations)
    new_timestamp = old_utc_timestamp
    try:
        for device in devices:
            print(
                device["device_name"],
                device["device_id"],
                device["sensor_type_name"],
                device["sensor_id"],
                device["sensor_field_names"],
            )
            if device["device_name"] == device_name_auctual:
                w = lacrosse_get_weather_data(token, device)
                push_all_since_timestamp_to_wunderground(w, old_utc_timestamp)
                new_timestamp = w["Temperature"]["values"][-1]["u"]
                # print(w)
    except Exception:
        # Ignore all errors, just retry again later with your automation
        pass
    print(new_timestamp)
