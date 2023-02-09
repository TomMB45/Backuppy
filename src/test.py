import tkinter
from tkinter import filedialog
import os 
import shutil

def parcourir(src = True) : 
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
    if src : 
        folder_path = filedialog.askdirectory(initialdir="C:\\Users\\Tom\\Documents\\", title="Choose a folder to copy")
    else : 
        folder_path = filedialog.askdirectory(initialdir="D:", title="Choose a folder to paste")
    return folder_path

def check_folder(src_folder_path, dest_folder_path) : 
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
    files = os.listdir(src_folder_path)
    for file in files :

        if os.path.isfile(os.path.join(src_folder_path, file)) : # Test if the file is a file
            ## Check if the file already exists and if the metadata are the same (os.path.getctime)
            if os.path.exists(os.path.join(dest_folder_path, file) # Test if the file already exists
                ) and os.path.getmtime(os.path.join(src_folder_path, file)) == os.path.getmtime(os.path.join(dest_folder_path, file) # Test if the metadata are the same
                ) and os.path.getsize(os.path.join(src_folder_path, file)) == os.path.getsize(os.path.join(dest_folder_path, file)) : # Test if the size is the same
                print(file, "already exists and will not be copied")
                continue

            else : # If the file does not exist or if the metadata are not the same
                shutil.copy2(os.path.join(src_folder_path, file), os.path.join(dest_folder_path, file))
                print(file, "copied")

        else : # If the file is a folder
            if not os.path.exists(os.path.join(dest_folder_path, file)) :
                os.mkdir(os.path.join(dest_folder_path, file))
            check_folder(os.path.join(src_folder_path, file), os.path.join(dest_folder_path, file))

if __name__ == "__main__" :
    src_folder = parcourir()
    dest_folder = parcourir(src=False)
    check_folder(src_folder_path=src_folder, dest_folder_path=dest_folder)