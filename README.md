# Backuppy
Tools for automatic backup 

## Installation
You require Python 3.8 or newer installed on your system. In case you do not have Python installed, we recommend installing Miniconda `<https://docs.conda.io/en/latest/miniconda.html>`.

Options to install backuppy are:

<!-- Install the latest release of greatpy from PyPI `<https://pypi.org/project/greatpy/>`:
``` bash
pip install Backuppy
``` -->

Install the latest development version:
``` bash
pip install git+https://github.com/TomMB45/Backuppy.git@main
```

## What is backuppy?
Backuppy is a Python package that provides tools for automatic backup. It is designed to be used in a cronjob or similar.

## How to use backuppy?
If you have installed backuppy, you can use it in your Python scripts. For example:
* double tap on the file `backup.py` in the folder `src` to run the script
* an explorer window will open, where you can select the folder you want to backup
* a second explorer window will open, where you can select the folder where you want to save the backup
* 2 output in the cmd output : 
    - `name_file copied` if the file is copied in the destination backup folder 
    - `name_file already exists and will not be copied` in some case : 
        - if the file is already in the destination backup folder
        - if the file is in the destination backup folder the metadata are the same as the file to copy

## How to contribute?
If you want to contribute to backuppy, you can do so by forking the repository and creating a pull request. Please make sure that your code is well documented and that you have added tests for your code.
You can also contribute by reporting bugs or suggesting new features by creating a new [issue](https://github.com/TomMB45/Backuppy/issues).