# Exchange Rates

App for getting data: CB RF Key Rate, USD/RUB, EUR/RUB, CNY/RUB exchange rates.

## Contents

- [Requirements](#requirements)
- [Quick start](#quick-start)
- [Configuration](#configuration)
- [Creating exe](#creating-exe)
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

| Key      | Description                                                                                                                                                                                                                                                                                                                                                              | Default value |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| platform | The platform you are running code on.<br/> Possible: <br/> Console - the output will be in default console of the platform.<br/> Windows - the program will create tray icon, which will show interface on click. **If you run main.exe, you should state this in config.**<br/> Other - the program will try to show window, otherwise - the output will be in console. | "Console"     |

## Creating exe

If you change something in code and want to make new `.exe` file, in the project folder type:

```bash
pyinstaller --paths . -i ".\assets\cb_logo.ico" --onefile -w .\scripts\main.py
```

Once the process finished, move `main.exe` from `dist` folder to the project folder.
Folders named `dist` and `build` you can delete as well as `main.spec` file, they're temporary.

#### Explanation

- `--paths .` adds project folder to exe creation in order not to break python imports;
- `-i ".\assets\cb_logo.ico"` adds logo for executable, which located in `assets` folder;
- `--onefile` means, that there will be no extra files with sources;
- `-w` means, that the executable will run hiding console, like many other Windows apps;
- `.\scripts\main.py` is a path to program entry point.

## Technologies

- [Python](https://www.python.org/)
- [Qt (PyQt)](https://www.qt.io/)
- [aiohttp](https://docs.aiohttp.org/en/stable/)
- [pyinstaller](https://pyinstaller.org/en/stable/index.html)

## File structure

Coming soon...

## Testing

Make sure you have installed `pytest` package (it is also stated in `requirements.txt`).

To run all the tests use:

```bash
pytest -v
```