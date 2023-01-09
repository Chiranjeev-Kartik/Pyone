import tkinter as tk
from tkinter import filedialog


class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.menu = None
        self.scrollbar = None
        self.text = None
        self.file_menu = None
        self.create_widgets()

    def create_widgets(self):
        # Create the text widget
        self.text = tk.Text(self, font=('Helvetica', 12))
        self.text.pack(side='top', fill='both', expand=True)

        # Create the scrollbar
        self.scrollbar = tk.Scrollbar(self, orient='vertical', command=self.text.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.text.config(yscrollcommand=self.scrollbar.set)

        # Create the file menu
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='New', command=self.new_file)
        self.file_menu.add_command(label='Open', command=self.open_file)
        self.file_menu.add_command(label='Save', command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self.exit)

    def new_file(self):
        self.text.delete('1.0', 'end')

    def open_file(self):
        filepath = tk.filedialog.askopenfilename()
        if filepath:
            with open(filepath, 'r') as file:
                self.text.delete('1.0', 'end')
                self.text.insert('1.0', file.read())

    def save_file(self):
        filepath = tk.filedialog.asksaveasfilename()
        if filepath:
            with open(filepath, 'w') as file:
                file.write(self.text.get('1.0', 'end'))

    def exit(self):
        self.destroy()


app = TextEditor()
app.mainloop()
