import tkinter as tk
from tkinter import messagebox
import json

# Load tasks from file
def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

# Add task to the list
def add_task():
    description = description_entry.get()
    deadline = deadline_entry.get()
    if description and deadline:
        tasks.append({"description": description, "deadline": deadline, "completed": False})
        save_tasks(tasks)
        update_task_list()
        description_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Input Error", "Both description and deadline are required.")

# Mark task as completed
def mark_completed():
    try:
        selected_task = task_listbox.curselection()[0]
        tasks[selected_task]['completed'] = True
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showerror("Selection Error", "Please select a task to mark as completed.")

# Update task list display
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "Done" if task['completed'] else "Pending"
        task_listbox.insert(tk.END, f"{task['description']} - {task['deadline']} - {status}")

# Initialize the Tkinter window
root = tk.Tk()
root.title("To-Do List")

tasks = load_tasks()

# Create and place widgets
description_label = tk.Label(root, text="Task Description")
description_label.pack()

description_entry = tk.Entry(root, width=40)
description_entry.pack()

deadline_label = tk.Label(root, text="Deadline (YYYY-MM-DD)")
deadline_label.pack()

deadline_entry = tk.Entry(root, width=40)
deadline_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack()

mark_button = tk.Button(root, text="Mark Completed", command=mark_completed)
mark_button.pack()

# Initial update of the task list
update_task_list()

# Start the Tkinter main loop
root.mainloop()
