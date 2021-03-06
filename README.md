[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
<!--- [![LinkedIn][linkedin-shield]][linkedin-url] --->




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/manofthemountain/lacrosseview-to-wunderground">
    <img src="images/logo.png" alt="Logo" width="160" height="80">
  </a>

<h3 align="center">Lacrosse View to Wunderground</h3>

  <p align="center">
    Connects your Lacrosse weather station to your Weather Underground Personal Weather Station (PWS) Network
    <br />
    <a href="https://github.com/manofthemountain/lacrosseview-to-wunderground"><strong>Explore the docs »</strong></a>
    <br />
    <br />    ·
    <a href="https://github.com/manofthemountain/lacrosseview-to-wunderground/issues">Report Bug</a>
    ·
    <a href="https://github.com/manofthemountain/lacrosseview-to-wunderground/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!--- [![Product Name Screen Shot][product-screenshot]](https://example.com)  --->

Not all La Crosse weather stations are integrated with Weather Underground Personal Weather Station (PWS) Network.  Lacrosse relies on its own app, La Crosse View, and cloud storage for viewing and collecting your weather.  This project allows you to access your weather data stored on the La Crosse servers and publish it to a Weather Underground.

#### Supported La Crosse Systems
#####  Tested
- [x] V61 Complete Personal Remote Monitoring Wi-Fi Weather Station

#####  Unknown
- [ ] VA1 Wi-Fi Projection Alarm Clock with Outdoor Temp and Humidity
- [ ] 328-10618V2 Complete Personal Wi-Fi Weather Station with AccuWeather
- [ ] V40A-PROV2 Complete Personal Remote Monitoring Weather Station
- [ ] V21-WTHV3 Complete Personal Wireless Remote Monitoring Wind Station
- [ ] V11 Wireless Wi-Fi Weather Station
- [ ] V22-WRTHV2 Complete Personal Remote Monitoring Weather Station
- [ ] V10V2 Wireless Wi-Fi Weather Station
- [ ] V50 Wi-Fi Wind and Weather Station
- [ ] C79790 WiFi Weather Station
- [ ] C82929V2 WiFi Projection Alarm Clock with AccuWeather
- [ ] V51 Wi-Fi Weather Station with AccuWeather Forecast


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [AWS](https://aws.amazon.com/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites


* python3
  * Check your python version on command line/terminal/shell.
  ```sh
  python --version
  ```
* La Crosse View Account [Android](https://play.google.com/store/apps/details?id=com.lacrosseview.app) [iOS](https://apps.apple.com/us/app/la-crosse-view/id1006925791)
  * Account Email
  * Account Password
* Weather Underground Account
  * Setup Personal Weather Station
    * Station ID
    * Station Key
    * API key
* AWS Account


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/manofthemountain/lacrosseview-to-wunderground.git
   ```
2. TBD

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://github.com/manofthemountain/lacrosseview-to-wunderground/wiki)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Use AWS Lambda to host and run script
- [ ] Use AWS EventBridge to run script on schedule
- [ ] Store credentials in AWS Secrets Manager
- [ ] Query multiple sensors

<!--
- [ ] TBD
    - [ ] TBD Nested Feature
-->

See the [open issues](https://github.com/manofthemountain/lacrosseview-to-wunderground/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU GPLV3. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Ryan - 01medleys_mermaid@icloud.com

Project Link: [https://github.com/manofthemountain/lacrosseview-to-wunderground](https://github.com/manofthemountain/lacrosseview-to-wunderground)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [keithprickett/lacrosse_weather](https://github.com/keithprickett/lacrosse_weather)
* [dbconfession78/py_weather_station](https://github.com/dbconfession78/py_weather_station)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/manofthemountain/lacrosseview-to-wunderground.svg?style=for-the-badge
[contributors-url]: https://github.com/manofthemountain/lacrosseview-to-wunderground/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/manofthemountain/lacrosseview-to-wunderground.svg?style=for-the-badge
[forks-url]: https://github.com/manofthemountain/lacrosseview-to-wunderground/network/members
[stars-shield]: https://img.shields.io/github/stars/manofthemountain/lacrosseview-to-wunderground.svg?style=for-the-badge
[stars-url]: https://github.com/manofthemountain/lacrosseview-to-wunderground/stargazers
[issues-shield]: https://img.shields.io/github/issues/manofthemountain/lacrosseview-to-wunderground.svg?style=for-the-badge
[issues-url]: https://github.com/manofthemountain/lacrosseview-to-wunderground/issues
[license-shield]: https://img.shields.io/github/license/manofthemountain/lacrosseview-to-wunderground.svg?style=for-the-badge
[license-url]: https://github.com/manofthemountain/lacrosseview-to-wunderground/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
