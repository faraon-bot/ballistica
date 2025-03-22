# Ballistica Project Configuration

This directory contains overall configuration files for the project.

Noteworthy files:
- [projectconfig.json](projectconfig.json): Top level settings for the project.
  Various tools look for values here.
- [spinoffconfig.py](spinoffconfig.py): Configures how this project can be
  spun off into other projects and/or what it inherits from a parent project.
- **localconfig.json**: Optional file influencing behavior only at this
  location. This file should not be stored in git/etc.

## Setting Up the Python Virtual Environment

To set up the Python virtual environment for this project, follow these steps:

1. Ensure you have Python 3.12 installed on your system. You can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

2. Create a virtual environment in the project directory by running the following command:
   ```sh
   python3.12 -m venv .venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```sh
     .venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source .venv/bin/activate
     ```

4. Install the required Python packages by running:
   ```sh
   pip install -r config/requirements.txt
   ```

5. The virtual environment is now set up and ready to use.

## Using the Python Virtual Environment

Once the Python virtual environment is set up, you can use it to run various commands and scripts within the project. Here are some common tasks:

### Running Python Scripts

To run a Python script within the virtual environment, simply activate the virtual environment (if not already activated) and run the script using the `python` command. For example:
```sh
source .venv/bin/activate
python path/to/your_script.py
```

### Installing Additional Packages

If you need to install additional Python packages, you can do so using the `pip` command. For example:
```sh
pip install package_name
```

### Upgrading Packages

To upgrade the installed packages to their latest versions, you can use the `venv-upgrade` target in the `Makefile`. Run the following command:
```sh
make venv-upgrade
```

### Cleaning the Virtual Environment

If you need to remove the virtual environment and start fresh, you can use the `venv-clean` target in the `Makefile`. Run the following command:
```sh
make venv-clean
```

### Deactivating the Virtual Environment

To deactivate the virtual environment, simply run:
```sh
deactivate
```
