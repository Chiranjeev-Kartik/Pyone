import os
import tkinter as tk
import tkinter.filedialog as tkfiledialog

"""The script creates a simple file search utility using the Tkinter widget toolkit. The utility has two widgets: a 
label and entry for the search string, and a button to initiate the search process. When the user clicks the search 
button, the utility prompts the user to select a directory using the askdirectory method of the tkinter.filedialog 
module. It then searches for files in the selected directory that match the search string using the os.walk function 
and a search_filter function that checks if the search string is present in the filenames. The matching files are 
displayed in a list widget. """


def search_filter(filename, search):
    # Check if the search string is in the filename
    if search in filename:
        return True
    return False


class FileSearcher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.search_button = None
        self.search_entry = None
        self.search_label = None
        self.results_list = None
        self.create_widgets()

    def create_widgets(self):
        # Create the label and entry for the search string
        self.search_label = tk.Label(self, text='Search:', font=('Helvetica', 12))
        self.search_label.pack(side='left', padx=10, pady=10)
        self.search_entry = tk.Entry(self, font=('Helvetica', 12))
        self.search_entry.pack(side='left', padx=10, pady=10)

        # Create the search button
        self.search_button = tk.Button(self, text='Search', font=('Helvetica', 12), command=self.search_files)
        self.search_button.pack(side='left', padx=10, pady=10)

        # Create the list widget to display the search results
        self.results_list = tk.Listbox(self, font=('Helvetica', 12))
        self.results_list.pack(side='left', padx=10, pady=10)

    def search_files(self):
        # Clear the previous search results
        self.results_list.delete(0, 'end')

        # Get the search string
        search = self.search_entry.get()

        # Get the directory to search in
        directory = tkfiledialog.askdirectory()
        if not directory:
            return

        # Search the files
        for root, dirs, files in os.walk(directory):
            # Filter the list of files
            files = filter(lambda x: search_filter(x, search), files)

            # Add the matching files to the results list
            for filename in files:
                self.results_list.insert('end', os.path.join(root, filename))


app = FileSearcher()
app.mainloop()
