# Backuppy
### Tools for automatic backup 

## What is backuppy?
Backuppy is a Python package that provides tools for automatic backup. It is designed to be used in a cronjob or similar.


## Installation
You require Python 3.8 or newer installed on your system. In case you do not have Python installed, we recommend installing Miniconda `<https://docs.conda.io/en/latest/miniconda.html>`.

To use backuppy, you can download the [code](https://github.com/TomMB45/Backuppy/archive/refs/heads/main.zip)

To install the latest development version :
``` bash
pip install git+https://github.com/TomMB45/Backuppy.git@main
```

You can also fork the repository and install the package in editable mode. 


## How to use backuppy?
If you have installed backuppy, you can use it in your Python scripts. 
For example :
* Double tap on the file `backup.py` to run the script
* An explorer window will open, where you can select the folder you want to backup
* A second explorer window will open, where you can select the folder where you want to save the backup
* 2 output in the cmd output : 
    - `name_file copied` if the file is copied to the destination backup folder 
    - `name_file already exists and will not be copied` in some cases: 
        - If the file is already in the destination backup folder
        - If the file is in the destination backup folder the metadata is the same as the file to copy

## How to contribute?
If you want to contribute to backuppy, you can do so by forking the repository and creating a pull request. Please make sure that your code is well documented and that you have added tests for your code.
You can also contribute by reporting bugs or suggesting new features by creating a new [issue](https://github.com/TomMB45/Backuppy/issues).
