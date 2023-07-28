#!/usr/bin/python

import os
import subprocess

source_folder = input("Path to the folder with .paq9a files: ")

# Get a list of all files in the source folder

file_paths = [os.path.join(source_folder, file) for file in os.listdir(source_folder)]

# Define the command to be executed with 'paq9a.exe x'

command = ["paq9a.exe", "x"]

# Loop through each file path and execute the command for each file

for file_path in file_paths:

    command.append(file_path)
    subprocess.run(command)
    command.pop() 

print("Extraction completed for all files.")
