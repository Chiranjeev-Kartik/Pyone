import tkinter as tk


class ToDoList(tk.Tk):
    def __init__(self):
        super().__init__()
        self.input_field = None
        self.delete_button = None
        self.scrollbar = None
        self.list_widget = None
        self.list_frame = None
        self.add_button = None
        self.create_widgets()

    def create_widgets(self):
        # Create the text input widget
        self.input_field = tk.Entry(self, font=('Helvetica', 24), bd=2, relief='groove')
        self.input_field.pack(side='top', fill='x', padx=10, pady=10)

        # Create the add button
        self.add_button = tk.Button(self, text='Add', font=('Helvetica', 24), bd=2, relief='groove',
                                    command=self.add_task)
        self.add_button.pack(side='top', padx=10, pady=10)

        # Create the list widget
        self.list_frame = tk.Frame(self)
        self.list_frame.pack(side='top', fill='both', expand=True)
        self.list_widget = tk.Listbox(self.list_frame, font=('Helvetica', 24), bd=0, selectmode='single')
        self.list_widget.pack(side='left', fill='both', expand=True)
        self.scrollbar = tk.Scrollbar(self.list_frame, orient='vertical', command=self.list_widget.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.list_widget.config(yscrollcommand=self.scrollbar.set)

        # Create the delete button
        self.delete_button = tk.Button(self, text='Delete', font=('Helvetica', 24), bd=2, relief='groove',
                                       command=self.delete_task)
        self.delete_button.pack(side='top', padx=10, pady=10)

    def add_task(self):
        task = self.input_field.get()
        if task:
            self.list_widget.insert('end', task)
            self.input_field.delete(0, 'end')

    def delete_task(self):
        selection = self.list_widget.curselection()
        if selection:
            self.list_widget.delete(selection[0])


app = ToDoList()
app.mainloop()
