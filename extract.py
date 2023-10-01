#!/usr/bin/python

import os
import subprocess
import threading

# Functio to extract all the files passed

def extract_file(file_path):
    
    command = ["paq9a.exe", "x", file_path]
    os.system(command)

# Ask the user to input the file directory

source_folder = input("Path to the folder with .paq9a files: ")

# Get a list of all files in the source folder

file_paths = [os.path.join(source_folder, file) for file in os.listdir(source_folder)]

thread_list = []

# Loop through each file path and execute the command for each file

for file_path in file_paths:

    thread = threading.Thread(target=extract_file, args=(file_path,))
    thread_list.appends(thread)
    thread.start()

# Wait for the threads to finish

for thread in thread_list:

    thread.join()
    
print("Extraction completed for all files.")
