import os

def file_renaming():
    path = input("Please enter the path of files : ")
    filename = input("Please enter the filename : ")
    files = os.listdir(path)
    for count, file in enumerate(files):
        new_name = str(filename) + "__" + str(int(count) + 1) + ".jpg"
        source = path + file
        destination = path + new_name
        os.rename(source, destination)

# Calling the functions to rename files

file_renaming()

# Important note : Enter a frontslash(\) sign at the end of file path
