import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)

def mark_completed():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.itemconfig(selected_task_index, {'fg': 'gray'})

# Create the main application window
app = tk.Tk()
app.title("To-Do List")

# Create and configure the widgets
entry = tk.Entry(app, width=50)
add_button = tk.Button(app, text="Add Task", command=add_task)
remove_button = tk.Button(app, text="Remove Task", command=remove_task)
completed_button = tk.Button(app, text="Mark Completed", command=mark_completed)
tasks_listbox = tk.Listbox(app, selectmode=tk.SINGLE, width=60)

# Place the widgets using grid layout
entry.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
tasks_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
add_button.grid(row=2, column=0, padx=5, pady=5)
remove_button.grid(row=2, column=1, padx=5, pady=5)
completed_button.grid(row=2, column=2, padx=5, pady=5)

# Start the main event loop
app.mainloop()
