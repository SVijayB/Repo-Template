# repo-template

<p align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.png">
        <img alt="Switcher for light and dark mode" src="assets/logo.png">
    </picture>
    <br>Short description of the project
</p>

---

<p align="center">
    <a href="https://github.com/svijayb/repo-template/pulls">
        <img src="https://img.shields.io/github/issues-pr/svijayb/repo-template.svg?style=for-the-badge&amp;logo=opencollective" alt="GitHub pull-requests">
    </a>
<a href="https://github.com/svijayb/repo-template/issues">
    <img src="https://img.shields.io/github/issues/svijayb/repo-template.svg?style=for-the-badge&amp;logo=testcafe" alt="GitHub issues">
    </a>
<a href="https://github.com/svijayb/repo-template/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/svijayb/repo-template.svg?style=for-the-badge&amp;logo=bandsintown" alt="GitHub contributors">
    </a>
<a href="https://github.com/svijayb/repo-template/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/svijayb/repo-template?style=for-the-badge&amp;logo=appveyor" alt="GitHub license">
    </a>
<a href="https://github.com/svijayb/repo-template">
    <img src="https://img.shields.io/github/repo-size/svijayb/repo-template?style=for-the-badge&amp;logo=git" alt="GitHub repo size">
    </a>
<a href="https://github.com/svijayb/repo-template/blob/main/.github/CODE_OF_CONDUCT.md">
    <img src="https://img.shields.io/badge/code%20of-conduct-ff69b4.svg?style=for-the-badge&amp;logo=crowdsource" alt="Code of Conduct">
    </a>
<a href="https://github.com/svijayb/repo-template/blob/main/.github/CONTRIBUTING.md">
    <img src="https://img.shields.io/static/v1?style=for-the-badge&amp;logo=opensourceinitiative&amp;label=Open&amp;message=Source%20%E2%9D%A4%EF%B8%8F&amp;color=blueviolet" alt="Open Source Love svg1">
    </a>
</p

## 🗺️ Map

- [<code>📖 Motivation</code>](#-motivation)
- [<code>📦 Installation</code>](#-installation)
- [<code>🚀 Usage</code>](#-usage)
- [<code>🤝 Contributing</code>](#-contributing)
- [<code>📝 License</code>](#-license)

## 📖 Motivation

<p align="center">
    <img src="https://i.pinimg.com/originals/4a/65/ab/4a65abeead3a8d113bccfee5d5d239f4.gif">
</p>

$$\color{#00BFFF}Purpose$$

In order to easily create a new project, I have created a standard template for all my projects.

$$\color{#00BFFF}Features \space \color{#56565E}Included$$

- Issue templates
- Pull request templates
- Contributing guidelines
- Code of conduct
- Required resources to help people start contributing
- README.md file with a basic setup

$$\color{#00BFFF}Quick \space \color{#56565E}Start$$

Simply search and replace `repo-template` with the name of your project.

Or, use the automation script:

```bash
python assets/replace-name.py
```

Don't forget to change the logo and the demo video in the README.md file!

## 📦 Installation

$$\color{#00BFFF}Clone \space \color{#56565E}Repository$$

```bash
git clone https://github.com/svijayb/repo-template
cd repo-template
```

$$\color{#00BFFF}Install \space \color{#56565E}Prerequisites$$

This project uses [uv](https://github.com/astral-sh/uv) for fast, reliable Python package management. Install it with:

```bash
pip install uv
```

$$\color{#00BFFF}Setup \space \color{#56565E}Environment$$

Create a virtual environment and install all requirements.
Make sure to update the `pyproject.toml` file with your project name and description!

```bash
uv sync
```

Before we can run the script, let's make sure to setup environment variables.

```bash
cp .env.example .env
```

Then, update the `.env` file with the relevant values.

## 🚀 Usage

$$\color{#00BFFF}Launch \space \color{#56565E}Application$$

To launch the application, use:

```bash
uv run main.py
```

$$\color{#00BFFF}Project \space \color{#56565E}Demo$$

![Project demo](https://media2.giphy.com/media/v1.Y2lkPTZjMDliOTUycDUybHhzNHYxbW1hYTQ5bnd5MHRyMjQzbHU5MnNobDZ3NDc3M3dzYyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/11sBLVxNs7v6WA/giphy.gif)

You can also find the demo video [here](https://www.youtube.com/watch?v=dQw4w9WgXcQ).

## 🤝 Contributing

$$\color{#00BFFF}How \space \color{#56565E}to \space Contribute$$

To contribute to repo-template, fork the repository, create a new branch and send us a pull request.
Make sure you read [CONTRIBUTING.md](.github/CONTRIBUTING.md) before sending us Pull requests.

Thanks for contributing to Open-source! ❤️

## 📝 License

This project is licensed under the MIT License. Read the [LICENSE](LICENSE) file for details.


```
██╗    ██╗███████╗    ██╗      ██████╗ ██╗   ██╗███████╗      ██╗██████╗                 
██║    ██║██╔════╝    ██║     ██╔═══██╗██║   ██║██╔════╝     ██╔╝╚════██╗                
██║ █╗ ██║█████╗      ██║     ██║   ██║██║   ██║█████╗      ██╔╝  █████╔╝                
██║███╗██║██╔══╝      ██║     ██║   ██║╚██╗ ██╔╝██╔══╝      ╚██╗  ╚═══██╗                
╚███╔███╔╝███████╗    ███████╗╚██████╔╝ ╚████╔╝ ███████╗     ╚██╗██████╔╝                
 ╚══╝╚══╝ ╚══════╝    ╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝      ╚═╝╚═════╝                 
                                                                                         
 ██████╗ ██████╗ ███████╗███╗   ██╗    ███████╗ ██████╗ ██╗   ██╗██████╗  ██████╗███████╗
██╔═══██╗██╔══██╗██╔════╝████╗  ██║    ██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔════╝
██║   ██║██████╔╝█████╗  ██╔██╗ ██║    ███████╗██║   ██║██║   ██║██████╔╝██║     █████╗  
██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║    ╚════██║██║   ██║██║   ██║██╔══██╗██║     ██╔══╝  
╚██████╔╝██║     ███████╗██║ ╚████║    ███████║╚██████╔╝╚██████╔╝██║  ██║╚██████╗███████╗
 ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝
```
