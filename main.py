import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")

        # Initialize history list
        self.history = []

        # Set dark theme colors
        bg_color = "#1e1e1e"
        fg_color = "#ffffff"
        button_bg_color = "#333333"
        button_fg_color = "#ffffff"
        display_bg_color = "#2e2e2e"
        display_fg_color = "#ffffff"

        # Set bold font
        bold_font = ('Arial', 14, 'bold')

        self.root.configure(bg=bg_color)

        self.display = tk.Entry(root, width=20, font=bold_font, borderwidth=15, relief="ridge", bg=display_bg_color, fg=display_fg_color)
        self.display.grid(row=0, column=0, columnspan=4, padx=15, pady=15)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '±', '√', '%',
            '^', '←', 'History'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(root, text=button, width=5, height=2, command=action, bg=button_bg_color, fg=button_fg_color, font=bold_font).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Bind keyboard events
        self.root.bind('<Key>', self.on_key_press)
        self.root.bind('<Return>', lambda event: self.on_button_click('='))
        self.root.bind('<BackSpace>', lambda event: self.on_button_click('←'))
        self.root.bind('<Escape>', lambda event: self.on_button_click('C'))
        self.root.bind('<%>', lambda event: self.on_button_click('%'))
        self.root.bind('<s>', lambda event: self.on_button_click('√'))
        self.root.bind('<p>', lambda event: self.on_button_click('±'))
        self.root.bind('<^>', lambda event: self.on_button_click('^'))
        self.root.bind('<h>', lambda event: self.on_button_click('History'))

    def on_button_click(self, button):
        if button == 'C':
            self.display.delete(0, tk.END)
        elif button == '←':
            self.display.delete(len(self.display.get())-1)
        elif button == '±':
            current_text = self.display.get()
            if current_text and current_text[0] == '-':
                self.display.delete(0)
            else:
                self.display.insert(0, '-')
        elif button == '√':
            try:
                value = float(self.display.get())
                result = math.sqrt(value)
                self.history.append(f"√{value} = {result}")
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))
        elif button == '%':
            try:
                value = float(self.display.get())
                result = value / 100
                self.history.append(f"{value}% = {result}")
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))
        elif button == '^':
            self.display.insert(tk.END, '**')
        elif button == '=':
            try:
                expression = self.display.get()
                result = eval(expression)
                self.history.append(f"{expression} = {result}")
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))
        elif button == 'History':
            self.show_history()
        else:
            self.display.insert(tk.END, button)

    def on_key_press(self, event):
        key = event.char
        if key.isdigit() or key in '+-*/.^':
            self.display.insert(tk.END, key)

    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("История расчетов")

        # Set dark theme colors for history window
        bg_color = "#1e1e1e"
        fg_color = "#ffffff"
        history_window.configure(bg=bg_color)

        # Create a text widget to display the history
        history_text = tk.Text(history_window, width=40, height=10, bg=bg_color, fg=fg_color, font=('Arial', 12, 'bold'))
        history_text.pack(padx=10, pady=10)

        # Insert the history into the text widget
        for entry in self.history:
            history_text.insert(tk.END, entry + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
