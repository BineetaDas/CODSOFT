import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    length = int(length_entry.get())
    
    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()
    
    character_set = ''
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_digits:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    password = ''.join(random.choice(character_set) for _ in range(length))
    password_display.config(text=password)

def clear_password():
    password_display.config(text="")

# Create the main application window
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x300")

# Password Length
length_label = tk.Label(app, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(app)
length_entry.pack()

# Character type checkboxes
lowercase_var = tk.BooleanVar()
lowercase_check = tk.Checkbutton(app, text="Lowercase", variable=lowercase_var)
lowercase_check.pack()

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(app, text="Uppercase", variable=uppercase_var)
uppercase_check.pack()

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(app, text="Digits", variable=digits_var)
digits_check.pack()

symbols_var = tk.BooleanVar()
symbols_check = tk.Checkbutton(app, text="Symbols", variable=symbols_var)
symbols_check.pack()

# Generate and display password button
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack()

# Password display label
password_display = tk.Label(app, text="", font=("Helvetica", 20))
password_display.pack()

# Clear password button
clear_button = tk.Button(app, text="Clear Password", command=clear_password)
clear_button.pack()

# Start the main event loop
app.mainloop()
