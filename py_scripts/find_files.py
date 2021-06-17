import os
import re 

def find_files():
    files_list = []
    inputpath = "."
    if os.path.isdir(os.path.abspath(inputpath)):
        fpath = os.path.abspath(inputpath)
        files_list = [os.path.join(directory, file) for directory, sub_dir, files in os.walk(fpath) for file in files if file.endswith('clean_config_result.json')]

    return files_list


print (find_files())
