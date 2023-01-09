import os
import tkinter as tk
import tkinter.filedialog as tkfiledialog

"""The script creates a simple file renaming utility using the Tkinter widget toolkit. The utility has three widgets: 
a label and entry for the search string, a label and entry for the replacement string, and a button to initiate the 
renaming process. When the user clicks the rename button, the utility prompts the user to select a directory using 
the askdirectory method of the tkinter.filedialog module. It then renames all the files in the selected directory by 
replacing the search string with the replacement string in the filenames. """


class FileRenamer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.rename_button = None
        self.replace_entry = None
        self.replace_label = None
        self.search_entry = None
        self.search_label = None
        self.create_widgets()

    def create_widgets(self):
        # Create the label and entry for the search string
        self.search_label = tk.Label(self, text='Search:', font=('Helvetica', 12))
        self.search_label.pack(side='left', padx=10, pady=10)
        self.search_entry = tk.Entry(self, font=('Helvetica', 12))
        self.search_entry.pack(side='left', padx=10, pady=10)

        # Create the label and entry for the replacement string
        self.replace_label = tk.Label(self, text='Replace:', font=('Helvetica', 12))
        self.replace_label.pack(side='left', padx=10, pady=10)
        self.replace_entry = tk.Entry(self, font=('Helvetica', 12))
        self.replace_entry.pack(side='left', padx=10, pady=10)

        # Create the rename button
        self.rename_button = tk.Button(self, text='Rename', font=('Helvetica', 12), command=self.rename_files)
        self.rename_button.pack(side='left', padx=10, pady=10)

    def rename_files(self):
        # Get the search and replacement strings
        search = self.search_entry.get()
        replace = self.replace_entry.get()

        # Get the directory to rename files in
        directory = tkfiledialog.askdirectory()
        if not directory:
            return

        # Rename the files
        for filename in os.listdir(directory):
            if search in filename:
                new_filename = filename.replace(search, replace)
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))


app = FileRenamer()
app.mainloop()
