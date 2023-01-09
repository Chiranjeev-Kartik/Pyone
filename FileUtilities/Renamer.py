import os

"""
Problem Statement:
Create a program that takes a directory as input and renames all the files in it based on a user-specified pattern.
For example, the user could specify that all the files should be renamed to "file_1.txt", "file_2.txt", etc.
"""

"""
Solution:
This code defines a function rename_files that takes two arguments: the source directory and the pattern for the new 
file names. The function iterates through all the files in the source directory and generates a new file name using
the pattern and the current file index (starting from 1). It then renames the file using the os.rename function.
"""


def rename_files(src_dir, pattern):
    # Iterate through all the files in the source directory
    for i, file in enumerate(os.listdir(src_dir)):
        # Construct the full path for the file
        src_path = os.path.join(src_dir, file)
        # Generate the new file name using the pattern and the current file index
        new_name = pattern.format(i+1)
        # Construct the full path for the new file name
        destination_path = os.path.join(src_dir, new_name)
        # Rename the file
        os.rename(src_path, destination_path)


# Test the function
_src_dir = ''
_pattern = 'file_{}.txt'
rename_files(_src_dir, _pattern)
