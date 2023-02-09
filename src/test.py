import tkinter
from tkinter import filedialog
import os 
import shutil

def parcourir(title="Choisir un dossier") : 
    """
    Function allowing to browse folders and choose a folder
    
    Parameters
    ----------
    None

    Returns
    -------
    folder_path : str
        Path of the chosen folder
    """

    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
    folder_path = filedialog.askdirectory(initialdir="D:", title=title)
    return folder_path


import glob

def check_folder(folder_path, dest_folder) : 
    """
    Recursive function to copy a folder and its content

    Parameters
    ----------
    folder_path : str
        Path of the folder to copy

    Returns
    -------
    None
    """
    files = os.listdir(folder_path)
    for file in files :
        if os.path.isfile(os.path.join(folder_path, file)) :
            print(file, "test") 
        else : 
            os.chdir(os.path.join(folder_path, file))
            os.mkdir(file)
            check_folder(os.path.join(folder_path, file))


# from distutils.dir_util import copy_tree

if __name__ == "__main__" :
    src_folder = parcourir(title="Choose a folder to copy")
    dest_folder = parcourir(title="Choose a folder to paste")
    files = os.listdir(src_folder)
    # print(files)
    for file in files :
        if os.path.isfile(os.path.join(src_folder, file)) :
            shutil.copy(os.path.join(src_folder, file), dest_folder)
            print(file, "copied")
        else : 
            files = check_folder(os.path.join(src_folder, file), dest_folder)
