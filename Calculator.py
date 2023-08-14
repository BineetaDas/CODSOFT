import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create a simple GUI window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the expression and results
entry = tk.Entry(root, font=("Helvetica", 20))
entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Buttons for calculator
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
    ("C")
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)
    for button_text in row:
        button = tk.Button(frame, text=button_text, font=("Helvetica", 20), relief=tk.RIDGE, borderwidth=1)
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        button.bind("<Button-1>", on_click)

# Start the main event loop
root.mainloop()

