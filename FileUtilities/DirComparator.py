import os

"""
Problem Statement:
A tool that compares the contents of two directories and reports any differences. This could be useful for detecting
changes in a set of files over time.
"""

"""
Solution: 
This script compares the files in the two directories (and their subdirectories) and returns a list of 
dictionaries, each containing the file path and reason for the difference (either 'only in dir1', 'only in dir2', 
or 'content differs'). The script can be modified to ignore certain file types or to compare the contents of 
directories with different structures, if desired. 
"""


def compare_directories(dir1, dir2):
    differences = []
    files1 = set(os.listdir(dir1))
    files2 = set(os.listdir(dir2))
    # Find files that are unique to dir1
    unique_to_dir1 = files1 - files2
    differences.extend([{'file': f, 'reason': 'only in dir1'} for f in unique_to_dir1])
    # Find files that are unique to dir2
    unique_to_dir2 = files2 - files1
    differences.extend([{'file': f, 'reason': 'only in dir2'} for f in unique_to_dir2])
    # Check for differences in common files
    common_files = files1 & files2
    for f in common_files:
        file1_path = os.path.join(dir1, f)
        file2_path = os.path.join(dir2, f)
        with open(file1_path, 'rb') as f1, open(file2_path, 'rb') as f2:
            if f1.read() != f2.read():
                differences.append({'file': f, 'reason': 'content differs'})
    return differences


# Example usage
_differences = compare_directories('/path/to/dir1', '/path/to/dir2')
for difference in _differences:
    print(f"{difference['file']} is {difference['reason']}")
