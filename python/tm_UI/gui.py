#this will incorporate some new techniques for a visual for the app
#we will be using tkinter

import tkinter as tk
from tkinter import messagebox
from tm import Task
from storage import Storage

class TaskManagerApp:
    def __init__(self):
        self.storage = Storage()
        self.tasks = self.storage.load_tasks()

        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.root.geometry("600x500")

        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=20)

        tk.Label(input_frame, text="Title:").grid(row=0, column=0, padx=5)
        self.title_entry = tk.Entry(input_frame, width=30)
        self.title_entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Category:").grid(row=1, column=0, padx=5, pady=5)
        self.category_entry = tk.Entry(input_frame, width=30)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Due Date (MM-DD-YYYY):").grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(input_frame, width=30)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Task", command=self.add_task).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Mark Complete", command=self.mark_complete).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete Task", command=self.delete_task).pack(side=tk.LEFT, padx=5)

        list_frame = tk.Frame(self.root)
        list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        tk.Label(list_frame, text="Tasks:", font=("Arial", 12, "bold")).pack()

        self.task_listbox = tk.Listbox(list_frame, width=70, height=15)
        self.task_listbox.pack(padx=10, pady=5)

        self.refresh_task_list()



    def add_task(self):
        title = self.title_entry.get()
        category = self.category_entry.get()
        due_date = self.date_entry.get()

        new_task = Task(title, category, due_date)
        self.tasks.append(new_task)

        self.storage.save_tasks(self.tasks)
        self.refresh_task_list()

    def mark_complete(self):
        selection = self.task_listbox.curselection()
        if not selection:
            return
        
        index = selection[0]
        self.tasks[index].mark_complete()

        self.storage.save_tasks(self.tasks)
        self.refresh_task_list()

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if not selection:
            return
        
        index = selection[0]
        del self.tasks[index]

        self.storage.save_tasks(self.tasks)
        self.refresh_task_list()

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task.completed else ""
            display_text = f"[{status}] {task.title} - {task.category} - Due: {task.due_date}"
            self.task_listbox.insert(tk.END, display_text)

if __name__ == "__main__":
    app = TaskManagerApp()
    app.root.mainloop()
