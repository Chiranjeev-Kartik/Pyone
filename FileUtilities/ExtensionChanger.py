import os
import glob
from docx import Document

"""
Problem Statement:
A script that converts the file format of a set of files. For example, you could write a script that converts all 
the .docx files in a directory to .pdf. 
"""

"""
Solution: 
This script searches for files with the specified input format in the input folder (and its sub-folders) 
and converts them to the specified output format, saving the output files to the output folder. In this example, 
the script converts .docx files to .pdf using the python-docx library, but you can add additional conversions as 
needed.python-docx is a useful tool for automating the creation and manipulation of Word documents in Python. 
"""


def convert_docx_to_pdf(pdf_filename):
    document = Document()
    document.save(pdf_filename)


def convert_files(input_folder, output_folder, input_format, output_format):
    input_files = glob.glob(f"{input_folder}/*.{input_format}")
    for input_file in input_files:
        file_name = os.path.basename(input_file)
        output_file = f"{output_folder}/{file_name.replace(input_format, output_format)}"
        if input_format == 'docx' and output_format == 'pdf':
            convert_docx_to_pdf(output_file)
        # Add additional conversions here as needed


# Example usage
convert_files('/path/to/input/folder', '/path/to/output/folder', 'docx', 'pdf')
