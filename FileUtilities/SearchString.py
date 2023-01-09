import os

"""
Problem Statement:
A utility that searches for a specific string of text within a set of files and returns the results in a structured
format.
"""

"""
Solution: 
This script will search all the files in the specified folder (and its sub-folders) for the search string 
and return a list of dictionaries, each containing the file path, line number, and matching line for each match 
found. The script can be modified to search for a regular expression or to search for matches in a case-insensitive 
way, if desired. 
"""


def search_files(folder, search_string):
    results = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                for i, line in enumerate(f):
                    if search_string in line:
                        result = {
                            'file': file_path,
                            'line': i+1,
                            'match': line.strip()
                        }
                        results.append(result)
    return results


# Example usage
_results = search_files('/path/to/folder', 'search string')
for _result in _results:
    print(f"Found '{_result['match']}' in {_result['file']} on line {_result['line']}")
