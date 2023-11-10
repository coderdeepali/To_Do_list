import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def add_todo():
    todo = todo_input.get()
    if todo:
        selected_item = todo_list.selection()
        if selected_item:
            parent_task = todo_list.item(selected_item, "text")
            todo_list.insert(parent_task, tk.END, text=f"• {todo}")
        else:
            todo_list.insert("", tk.END, text=f"• {todo}")
        todo_input.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_todo():
    selected_item = todo_list.selection()
    if selected_item:
        todo_list.delete(selected_item)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("To-Do List App")

# Styling
root.geometry("600x500")  # Increased width
root.configure(bg="#2C3E50")  # Background color: Dark Gray

# Fonts
title_font = ("Helvetica", 24, "bold")
label_font = ("Arial", 14)
entry_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")
task_font = ("Arial", 12)  # Increased font size for tasks

# Colors
primary_color = "#3498db"  # Blue
success_color = "#2ecc71"  # Green
danger_color = "#e74c3c"   # Red
background_color = "#2C3E50"  # Dark Gray
listbox_select_color = "#34495E"  # Lighter Dark Gray

# Create and configure labels
title_label = tk.Label(root, text="My To-Do List", font=title_font, bg=background_color, fg="#ECF0F1")  # Light Gray
input_label = tk.Label(root, text="Add a Task:", font=label_font, bg=background_color, fg="#ECF0F1")  # Light Gray
title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")  # Increased column span
input_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Create and configure the input and buttons
todo_input = tk.Entry(root, width=50, font=entry_font, bg="#ECF0F1")  # Increase width
add_button = tk.Button(root, text="Add Task", command=add_todo, bg=success_color, fg="#ECF0F1", font=button_font)  # Light Gray
delete_button = tk.Button(root, text="Delete Task", command=delete_todo, bg=danger_color, fg="#ECF0F1", font=button_font)  # Light Gray

todo_input.grid(row=1, column=1, padx=10, pady=5, ipadx=3, ipady=3, columnspan=2)  # Increase column span
add_button.grid(row=2,columnspan=2, column=0, padx=10, pady=10, ipadx=3, ipady=3, sticky="ew")
delete_button.grid(row=2, column=2, padx=10, pady=10, ipadx=3, ipady=3, sticky="ew")  # Adjust column position

# Create and configure the to-do list using ttk.Treeview
style = ttk.Style(root)
style.configure("Treeview.Heading", font=title_font)
style.configure("Treeview", font=task_font)

todo_list = ttk.Treeview(root, columns=("Task",), show="tree", height=10)
todo_list.heading("#0", text="Task")

todo_list.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")  # Increase column span

# Create a scrollbar for the Treeview
scrollbar = ttk.Scrollbar(root, orient="vertical", command=todo_list.yview)
todo_list.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=4, column=3, sticky="ns")  # Adjust column position

# Configure row and column weights for resizing
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)  # Add a new column weight

# Start the application
root.mainloop()
