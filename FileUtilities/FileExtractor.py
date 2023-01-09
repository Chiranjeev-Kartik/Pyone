import os
import shutil

"""
Problem Statement:
Create a program that takes a directory as input and searches for all files with a given extension (e.g. .txt, .docx).
The program should then create a new directory and move all the matching files into it.
"""

"""
Solution:
This code defines a function move_files that takes three arguments: the source directory, the destination directory,
and the file extension. The function first checks if the destination directory exists and creates it if it doesn't.
It then iterates through all the files in the source directory and checks if each file has the specified extension.
If it does, the file is moved to the destination directory using the shutil module.
"""


def move_files(src_dir, destination_dir, file_ext):
    # Check if the destination directory exists and create it if it doesn't
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Iterate through all the files in the source directory
    for file in os.listdir(src_dir):
        # Check if the file has the specified extension
        if file.endswith(file_ext):
            # Construct the full file path
            src_path = os.path.join(src_dir, file)
            destination_path = os.path.join(destination_dir, file)
            # Move the file to the destination directory
            shutil.move(src_path, destination_path)


# Test the function
_src_dir = '/path/to/source/directory'
_destination_dir = '/path/to/destination/directory'
_file_ext = '.txt'
move_files(_src_dir, _destination_dir, _file_ext)
