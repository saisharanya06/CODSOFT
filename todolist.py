import tkinter as tk
from tkinter import messagebox, simpledialog
import json

tasks_file = "tasks.json"

def load_tasks():
    try:
        with open(tasks_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(tasks_file, "w") as file:
        json.dump(tasks, file, indent=4)

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.tasks = load_tasks()
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(self.frame, width=50, height=10)
        self.listbox.pack(side=tk.LEFT, padx=(0, 10))

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.populate_listbox()

        self.entry = tk.Entry(self.root, width=54)
        self.entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Task", width=48, command=self.add_task)
        self.add_button.pack(pady=(0, 5))

        self.update_button = tk.Button(self.root, text="Update Task", width=48, command=self.update_task)
        self.update_button.pack(pady=(0, 5))

        self.done_button = tk.Button(self.root, text="Mark as Done", width=48, command=self.mark_task_done)
        self.done_button.pack(pady=(0, 5))

        self.delete_button = tk.Button(self.root, text="Delete Task", width=48, command=self.delete_task)
        self.delete_button.pack(pady=(0, 5))

    def populate_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task["done"] else "Not Done"
            self.listbox.insert(tk.END, f"{task['task']} - {status}")

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text:
            self.tasks.append({"task": task_text, "done": False})
            save_tasks(self.tasks)
            self.populate_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def update_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            new_task_text = simpledialog.askstring("Update Task", "Enter new task description:")
            if new_task_text:
                self.tasks[selected_task_index[0]]["task"] = new_task_text
                save_tasks(self.tasks)
                self.populate_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    def mark_task_done(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]["done"] = True
            save_tasks(self.tasks)
            self.populate_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

    def delete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            save_tasks(self.tasks)
            self.populate_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

