import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.display = None
        self.create_widgets()

    def create_widgets(self):
        # Create the display widget
        self.display = tk.Entry(self, font=('Helvetica', 24), justify='right', bd=5, relief='sunken', bg='#eee')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create the digit buttons
        digits = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['0', '.', '00']
        ]
        for i, row in enumerate(digits):
            for j, digit in enumerate(row):
                button = tk.Button(self, text=digit, font=('Helvetica', 24), width=5, bd=2, relief='groove',
                                   command=lambda _digit=digit: self.input_digit(_digit))
                button.grid(row=i + 1, column=j, padx=5, pady=5)

        # Create the operation buttons
        operations = [
            ['+', '-'],
            ['*', '/'],
            ['AC', 'C'],
            ['=']
        ]
        for i, row in enumerate(operations):
            for j, op in enumerate(row):
                button = tk.Button(self, text=op, font=('Helvetica', 24), width=5, bd=2, relief='groove',
                                   command=lambda _op=op: self.perform_operation(_op))
                button.grid(row=i + 1, column=j + 3, padx=5, pady=5)

    def input_digit(self, digit):
        self.display.insert(tk.END, digit)

    def perform_operation(self, op):
        if op == 'AC':
            self.display.delete(0, tk.END)
        elif op == 'C':
            self.display.delete(self.display.index(tk.END) - 1)
        elif op == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except ZeroDivisionError:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Error')
        else:
            self.display.insert(tk.END, op)


app = Calculator()
app.mainloop()
