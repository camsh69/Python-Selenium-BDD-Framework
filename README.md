# Python-Selenium-Behave-BDD

- Url, browser and headless option for chrome can be set in config/config.ini
- `behave` to run all tests
- `behave features/(name_of_feature).feature` to run specific feature file
- `behave -f allure_behave.formatter:AllureFormatter -o reports/ features` to run tests and then `allure serve reports/` to generate a report

#### TO DO

Add more BDD examples.

## Installs/Dependencies

### Download Python

https://www.python.org/downloads

Follow instructions of installer:

#### Windows

- Note the path where Python is being installed - generally C:\Users\(Your logged in User)\AppData\Local\Programs\Python\PythonXX

Set Python home in Environment Variables

- Do a search for 'Edit the system environment variables' in Windows
- Click on Environment Variables
- Edit 'Path'
- Set a new path to match the path where Python was installed
- Repeat above and add path for, e.g. C:\Users\(Your logged in User)\AppData\Local\Programs\Python\PythonXX/Scripts
- Open a new Command Prompt and enter: `python --version`
- If a response is returned then everything is installed fine

#### Mac

Path variable is set automatically by MacOS on install

- Open a new terminal and enter: `which python3`
- If a response is returned with a path then everything is installed OK

## Install Selenium

https://pypi.org/project/selenium

(PIP is a python package manager - https://pip.pypa.io/en/stable/)

#### Windows

- In CMD
- `pip install selenium`
- To check: `pip show selenium`

#### Mac

- In a terminal
- `pip3 install selenium`
- To check: `pip3 show selenium`

\*\* Make sure the browsers on your machine, e.g. Chrome, are updated to latest version (Selenium will throw errors if its version of, for example, Chromedriver doesn't match your version)

## Install Behave

https://behave.readthedocs.io/en/latest/install.html

#### Windows

- `pip install behave`

#### Mac

- `pip3 install behave`

## Install Allure Reports

https://pypi.org/project/allure-behave/

#### Windows

- `pip install allure-behave`

#### Mac

- `pip3 install allure-behave`

## Install a code editor

VS Code - https://code.visualstudio.com/download

- Install the following extensions
- Python (by Microsoft)
- Cucumber (by Cucumber)
- Cucumber (Gherkin) Full Support (by Alexander Krechik)

Pycharm - https://www.jetbrains.com/pycharm/download/ Free Community version

- Install the following plugin
- Gherkin (by Jetbrains)
