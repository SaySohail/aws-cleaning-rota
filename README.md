
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/SaySohail/aws-cleaning-rota ">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">WhatsApp Cleaning Rota Notifier</h3>

  <p align="center">
    ## Description
The WhatsApp Cleaning Rota Notifier is a serverless solution designed to automate the process of sending cleaning task reminders. Leveraging AWS Lambda and the Twilio API, this project efficiently notifies individuals of their scheduled cleaning duties according to a predefined rota, ensuring timely task completion and effective communication.

## Features
- **Automated WhatsApp Notifications**: Sends reminders for cleaning tasks directly to individuals' WhatsApp.
- **Serverless Architecture**: Utilizes AWS Lambda for running the application without the need for server management.
- **Scheduled Triggering**: Employs AWS EventBridge for timely execution of the function on specified days and times.
- **Twilio WhatsApp Integration**: Relies on Twilio API for seamless and reliable messaging.
- **Excel-based Rota Management**: Easy to manage and update the cleaning schedule through an Excel file.
- **Environment Friendly**: Reduces the need for paper-based schedules and manual follow-ups.

## How It Works
1. **Rota Schedule**: An Excel file (`Rota-Berkshire.xlsx`) contains the cleaning schedule, assigning tasks to individuals.
2. **Function Trigger**: AWS EventBridge triggers the Lambda function on pre-set days (Mondays and Thursdays at 9 AM UTC).
3. **Message Dispatch**: Upon execution, the Lambda function reads the schedule and sends WhatsApp messages to the designated individuals.

## Setup and Deployment

### Prerequisites
- AWS account with access to Lambda and EventBridge services.
- Twilio account with a WhatsApp-enabled phone number.
- Python environment for local setup.

### Dependencies
- `openpyxl` for Excel file handling.
- `requests` for making HTTP requests.
- `twilio` for Twilio API integration.

### Deployment Steps
1. **Prepare the Deployment Package**: Package the Python script along with its dependencies.
2. **Deploy to AWS Lambda**: Upload the package to AWS Lambda and configure the function.
3. **Set EventBridge Rules**: Configure rules to trigger the function as per the schedule.

## Configuration
- Set environment variables in AWS Lambda for Twilio credentials and phone numbers.
- Update the `Rota-Berkshire.xlsx` file to reflect the current schedule.

## Usage
Update the cleaning rota in the Excel file as needed, and the system will handle the rest, ensuring individuals receive timely notifications.

## Contributing
Contributions to the project are welcome. Please ensure to follow the best practices and coding standards.
    <br />
    <a href="https://github.com/SaySohail/aws-cleaning-rota "><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/SaySohail/aws-cleaning-rota ">View Demo</a>
    ·
    <a href="https://github.com/SaySohail/aws-cleaning-rota /issues">Report Bug</a>
    ·
    <a href="https://github.com/SaySohail/aws-cleaning-rota /issues">Request Feature</a>
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

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/SaySohail/aws-cleaning-rota .git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/SaySohail/aws-cleaning-rota /issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



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

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@SayedSohail10](https://twitter.com/SayedSohail10) - peerzadesayedsohail@gmail.com@gmail.com

Project Link: [https://github.com/SaySohail/aws-cleaning-rota ](https://github.com/SaySohail/aws-cleaning-rota )

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/SaySohail/aws-cleaning-rota .svg?style=for-the-badge
[contributors-url]: https://github.com/SaySohail/aws-cleaning-rota /graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/SaySohail/aws-cleaning-rota .svg?style=for-the-badge
[forks-url]: https://github.com/SaySohail/aws-cleaning-rota /network/members
[stars-shield]: https://img.shields.io/github/stars/SaySohail/aws-cleaning-rota .svg?style=for-the-badge
[stars-url]: https://github.com/SaySohail/aws-cleaning-rota /stargazers
[issues-shield]: https://img.shields.io/github/issues/SaySohail/aws-cleaning-rota .svg?style=for-the-badge
[issues-url]: https://github.com/SaySohail/aws-cleaning-rota /issues
[license-shield]: https://img.shields.io/github/license/SaySohail/aws-cleaning-rota .svg?style=for-the-badge
[license-url]: https://github.com/SaySohail/aws-cleaning-rota /blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/sayedsohail
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
