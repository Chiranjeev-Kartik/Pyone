import os

"""
Problem Statement:
A tool that splits a large file into smaller chunks for easier handling. This could be useful
for transferring large files over a network or for dividing a file for parallel processing.
"""

"""
Solution: 
This script reads the input file in chunks of the specified size and writes each chunk to a separate 
output file in the output folder. The output filenames are based on the name of the input file, with a chunk number 
appended to the end. 
"""


def split_file(input_file, output_folder, chunk_size):
    chunk_number = 1
    file_name, extension = os.path.splitext(input_file)
    with open(input_file, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            output_file = f"{output_folder}/{os.path.basename(input_file)}-{chunk_number}{extension}"
            print(output_file)
            with open(output_file, 'wb') as fw:
                fw.write(chunk)
            chunk_number += 1


# Example usage
split_file('/path/to/input/file', '/path/to/output/folder', 1024*1024*1024)  # Split into 1GB chunks
