# Exchange Rates

App for getting data: CB RF Key Rate, USD/RUB, EUR/RUB, CNY/RUB exchange rates.

## Contents

- [Requirements](#requirements)
- [Quick start](#quick-start)
- [Configuration](#configuration)
- [Technologies](#technologies)
- [File structure](#file-structure)
- [Testing](#testing)

## Requirements

To use the project, you need to install [Python 3](https://www.python.org/downloads/) (version 3.10 recommended).

## Quick start

### Installing virtual environment and libraries

Create virtual environment using bash console:

```bash
python3 -m venv YOUR_VIRTUAL_ENV_NAME
```

Activate virtual environment:

```bash
# Linux
source YOUR_VIRTUAL_ENV_NAME/bin/activate
# Windows
YOUR_VIRTUAL_ENV_NAME/Scripts/activate
```

Install necessary libraries:

```bash
pip install -r requirements.txt
```

### Running program

Execute entry point, called "main.py":

```bash
python main.py
```

## Configuration

In the `config.yaml` you can see configs for this project.

| Key      | Description                                                                                                                                                                                                                                                                                                    | Default value |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| platform | The platform you are running code on.<br/> Possible: <br/> Console - the output will be in default console of the platform.<br/> Windows - the program will create tray icon, which will show interface on click.<br/> Other - the program will try to show window, otherwise - the output will be in console. | "Console"     |

## Technologies

- [Python](https://www.python.org/)
- [Qt (PyQt)](https://www.qt.io/)

## File structure

Coming soon...

## Testing

Coming soon...