import subprocess
import time

"""
Problem Statement:
Python script that measures the execution time of a program from the command line.
"""

"""
Solution: 
This script uses the subprocess module to run the specified command and the time module to measure the 
elapsed time. The elapsed time is printed to the console in seconds. 
You can use this script by saving it to a file and running it with the command you want to measure as an argument. 
For example, to measure the execution time of a Python script called my_program.py, you would run the following 
command: 

python measure_execution_time.py "python my_program.py"
"""


def measure_execution_time(command):
    start = time.perf_counter()
    subprocess.run(command, shell=True)
    end = time.perf_counter()
    elapsed_time = end - start
    print(f"Elapsed time: {elapsed_time:.2f} seconds")


# Example usage
measure_execution_time("python file_path/file_name.py")
