import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Password length input
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack(pady=5)

        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=5)

        # Complexity selection
        self.complexity_label = tk.Label(root, text="Select Complexity:")
        self.complexity_label.pack(pady=5)

        self.complexity_var = tk.StringVar(value="Medium")
        self.complexity_combobox = Combobox(root, textvariable=self.complexity_var, values=["Low", "Medium", "High"])
        self.complexity_combobox.pack(pady=5)

        # Generate password button
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        # Display generated password
        self.password_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.password_label.pack(pady=10, anchor='center')  # Centered output label

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError("Length must be a positive integer.")
            complexity = self.complexity_var.get()
            password = self.create_password(length, complexity)
            self.password_label.config(text=password)
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def create_password(self, length, complexity):
        characters = ""
        if complexity == "Low":
            characters = string.ascii_lowercase + string.digits
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits
        elif complexity == "High":
            characters = string.ascii_letters + string.digits + string.punctuation

        if not characters:
            raise ValueError("Invalid complexity.")

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

