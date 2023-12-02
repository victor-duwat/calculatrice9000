import tkinter as tk
from tkinter import messagebox

class SimpleCalculatorGUI:
    def __init__(self, root):
        self.root = root
        root.title("Calculatrice Avancée")


        self.button_font = ('Verdana', 16)
        self.entry_font = ('Verdana', 18, 'bold')


        self.entry = tk.Entry(root, font=self.entry_font, width=15, borderwidth=5, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20)


        self.create_buttons()


        self.history = []

    def create_buttons(self):

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('0', 4, 0), ('+', 4, 1), ('-', 4, 2)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=self.button_font, width=5, height=2, 
                               command=lambda text=text: self.append_to_entry(text))
            button.grid(row=row, column=col, sticky="nsew")

        button_equal = tk.Button(self.root, text="=", font=self.button_font, width=5, height=2, 
                                 command=self.evaluate_expression)
        button_equal.grid(row=5, column=2, sticky="nsew")

        button_clear = tk.Button(self.root, text="C", font=self.button_font, width=5, height=2, 
                                 command=self.clear_entry)
        button_clear.grid(row=5, column=0, sticky="nsew")

        button_mul = tk.Button(self.root, text="*", font=self.button_font, width=5, height=2, 
                               command=lambda: self.append_to_entry(" * "))
        button_mul.grid(row=5, column=1, sticky="nsew")

        button_div = tk.Button(self.root, text="/", font=self.button_font, width=5, height=2, 
                               command=lambda: self.append_to_entry(" / "))
        button_div.grid(row=6, column=0, sticky="nsew")

        button_history = tk.Button(self.root, text="History", font=self.button_font, width=11, height=2, 
                                   command=self.show_history)
        button_history.grid(row=6, column=1, columnspan=2, sticky="nsew")

        for i in range(7):
            root.grid_rowconfigure(i, weight=1)
        for i in range(3):
            root.grid_columnconfigure(i, weight=1)

    def append_to_entry(self, value):
        self.entry.insert(tk.END, value)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def evaluate_expression(self):
        try:
            result = eval(self.entry.get())
            self.history.append(f"{self.entry.get()} = {result}")
            self.clear_entry()
            self.entry.insert(0, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            self.clear_entry()

    def show_history(self):
        history_string = "\n".join(self.history)
        messagebox.showinfo("History", history_string if history_string else "No history available")

root = tk.Tk()
calculator = SimpleCalculatorGUI(root)
root.mainloop()
