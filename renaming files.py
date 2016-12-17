import os
def rename_files():
    # getting the file name from a folder
    file_list=os.listdir(r"D:\prank")

    saved_path=os.getcwd()
    os.chdir(r"D:\prank")

    # rename each file name
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
rename_files()
