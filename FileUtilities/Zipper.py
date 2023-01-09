import os
import zipfile

"""
Problem Statement:
Write a program that takes a directory as input and creates a zip file for each subdirectory. The zip files should be 
named after the subdirectory and should contain all the files in the subdirectory.
"""

"""
Solution:
This code defines a function zip_subdirectories that takes a single argument: the source directory. 
The function uses the os.walk function to iterate through all the subdirectories in the source directory. 
For each subdirectory, it creates a zip file using the zipfile module and adds all the files in the subdirectory 
to the zip file.
"""


def zip_subdirectories(src_dir: str):
    # Iterate through all the subdirectories in the source directory
    for root, dirs, files in os.walk(src_dir):
        for d in dirs:
            # Construct the full path for the subdirectory
            subdir_path = os.path.join(root, d)
            # Create a zip file for the subdirectory
            zip_path = subdir_path + '.zip'
            zip_file = zipfile.ZipFile(zip_path, 'w')
            # Add all the files in the subdirectory to the zip file
            for f in os.listdir(subdir_path):
                file_path = os.path.join(subdir_path, f)
                zip_file.write(file_path, arcname=f)
            zip_file.close()


# Test the function
_src_dir = '/path/to/source/directory'
zip_subdirectories(_src_dir)
