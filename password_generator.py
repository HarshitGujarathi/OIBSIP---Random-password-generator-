import tkinter as tk
from tkinter import messagebox
import string
import random
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()
        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.lower_var = tk.IntVar()
        self.lower_check = tk.Checkbutton(root, text="Include Lowercase Letters", variable=self.lower_var)
        self.lower_check.pack()

        self.upper_var = tk.IntVar()
        self.upper_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.upper_var)
        self.upper_check.pack()

        self.digit_var = tk.IntVar()
        self.digit_check = tk.Checkbutton(root, text="Include Digits", variable=self.digit_var)
        self.digit_check.pack()

        self.symbol_var = tk.IntVar()
        self.symbol_check = tk.Checkbutton(root, text="Include Symbols", variable=self.symbol_var)
        self.symbol_check.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.show_button = tk.Button(root, text="Copy to Clipboard", command=self.show_password)
        self.show_button.pack()

        self.password_label = tk.Label(root, text="Your Password will appear here")
        self.password_label.pack()

    def generate_password(self):
        length = int(self.length_entry.get())
        include_lower = bool(self.lower_var.get())
        include_upper = bool(self.upper_var.get())
        include_digits = bool(self.digit_var.get())
        include_symbols = bool(self.symbol_var.get())

        if include_lower:
            characters = string.ascii_lowercase
        if include_upper:
            characters += string.ascii_uppercase
        if include_digits:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation

        if len(characters) == 0:
            messagebox.showerror("Error", "Please select at least one character type")
            return

        password = ''.join(random.choice(characters) for i in range(length))
        self.password_label.config(text=f"Your Password: {password}")
        self.generated_password = password

    def show_password(self):
        try:
            pyperclip.copy(self.generated_password)
            messagebox.showinfo("Password Copied", "Password copied to clipboard")
        except AttributeError:
            messagebox.showerror("Error", "No password generated yet")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
