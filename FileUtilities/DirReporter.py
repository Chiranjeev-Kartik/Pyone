import os

"""
Problem Statement:
Write a program that takes a directory as input and creates a report containing information about the files in the
directory. The report should include the file name, size, and last modified date for each file.
The program should be able to generate the report in HTML or CSV format.
"""

"""
Solution:
The code defines a function generate_report that takes two arguments: the source directory and the format of the report
(either 'html' or 'csv'). The function first collects the file name, size, and last modified date for each file
in the source directory and stores them in a list called report_data.

Next, the function generates the report based on the specified format. If the format is 'html', it generates an HTML 
table containing the report data.If the format is 'csv', it generates a CSV-formatted string containing the report data. 

Finally, the function returns the generated report. The caller can then use the returned report as needed, such as by 
printing it to the console or saving it to a file.
"""


def generate_report(src_dir, report_format):
    report_data = []
    # Iterate through all the files in the source directory
    for file in os.listdir(src_dir):
        # Get the file name, size, and last modified date
        file_name = file
        file_path = os.path.join(src_dir, file)
        file_size = os.path.getsize(file_path)
        file_modified_time = os.path.getmtime(file_path)
        # Add the data to the report data list
        report_data.append((file_name, file_size, file_modified_time))

    # Generate the report
    if report_format == 'html':
        # Generate the report in HTML format
        report = '<html>\n<head>\n<title>File Report</title>\n</head>\n<body>\n'
        report += '<table>\n<tr><th>Name</th><th>Size (bytes)</th><th>Modified</th></tr>\n'
        for file_name, file_size, file_modified_time in report_data:
            report += '<tr><td>{}</td><td>{}</td><td>{}</td></tr>\n'.format(file_name, file_size, file_modified_time)
        report += '</table>\n</body>\n</html>'

    elif report_format == 'csv':
        # Generate the report in CSV format
        report = 'Name,Size (bytes),Modified\n'
        for file_name, file_size, file_modified_time in report_data:
            report += '{},{},{}\n'.format(file_name, file_size, file_modified_time)
    else:
        raise ValueError('Invalid report format')

    return report


# Test the function
_src_dir = ''

# Generate a report in HTML format
report_html = generate_report(_src_dir, 'html')
print(report_html)
with open('report.html', 'w') as f:
    f.write(report_html)

# Generate a report in CSV format
report_csv = generate_report(_src_dir, 'csv')
print(report_csv)
with open('report.csv', 'w') as f:
    f.write(report_csv)
