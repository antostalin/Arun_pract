# Creating the Python Package Step-by-Step
Please go through the below documentation to understand the step-by-step guide to create the python package and testing in various ways

1. Creating the python package code
  - Install all required python packages
  - Write the python package code
  - Add python test file to validate the functionality
  - Create the requirements.txt for python dependency by using `pip freeze>requirements.txt` command
2. Required additional files for packaging
    - **setup.cfg** - It has configuration about the python packaging like metadata, options etc.
    - **pyproject.toml** - It has the build configuration
    - **MANIFEST.in** - It has the information about which files should be included in python packaging
    - **LICENSE** - It is a license file. The sample license content can get it from [license](https://choosealicense.com/) page
    - **README.md** - It is a documentation about the python package, and it's usage
3. Bundle, installation and validation can be done
  - locally
    - Go to the terminal and execute the `pip install .` command to install the current python package 
    - Type `python` in terminal then execute the `from image_ascii_arusteph import synthesize` command from REPL
    - If there are no issues in loading the python package then execute `exit()` command to exit from REPL
    - Python `build` package is necessary to build the python package. If it is not installed then execute `python -m pip install build` command
    - Execute the `python -m build` command for build and create the new *dist* directory
    - Uninstall the python package by executing `pip uninstall image_ascii_arusteph` command
  - test pypi
    - If you don't have any account in [Test PYPI](http://test.pypi.org) then login to [Test PYPI](http://test.pypi.org) page and register with new account
    - We need *twine* package to upload the python package to [Test PYPI](http://test.pypi.org) page. So, execute the `pip install twine` command to install the same
    - Upload the python package by `python -m twine upload --repository testpypi dist/*` command and also required to enter your credential to proceed the upload the content to the [Test PYPI](http://test.pypi.org) page
    - Once the upload was completed then index the python package from test pypi by executing `pip install -i https://test.pypi.org/simple image_ascii_arusteph` command from the terminal
    - Type `python` in terminal then execute the `from image_ascii_arusteph import synthesize` command from REPL
    - If there are no issues in loading the python package then execute `exit()` command to exit from REPL
    - Uninstall the python package by executing `pip uninstall image_ascii_arusteph` command
  - pypi
    - If you don't have any account in [PYPI](http://pypi.org) then login to [PYPI](http://pypi.org) page and register with new account
    - Upload the python package by `python -m twine upload --repository pypi dist/*` command and also required to enter your credential to proceed the upload the content to the [PYPI](http://pypi.org) page
    - Once the upload was completed then install the same by executing `pip install image_ascii_arusteph` command from the terminal
    - Type `python` in terminal then execute the `from image_ascii_arusteph import synthesize` command from REPL
    - If there are no issues in loading the python package then execute `exit()` command to exit from REPL
    - Uninstall the python package by executing `pip uninstall image_ascii_arusteph` command