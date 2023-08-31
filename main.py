import tkinter as tk


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.config(bg="grey", padx=10, pady=10)
        self.root.title("My To-Do List")

        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        self.add_task_button = tk.Button(root, text="Add", command=self.add_task)
        self.add_task_button.pack()

        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack()

        self.complete_button = tk.Button(root, text="Complete", command=self.mark_completed)
        self.complete_button.pack()

        self.delete_task = tk.Button(root, text="Delete", command=self.delete_task)
        self.delete_task.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.itemconfig(selected_task_index, {'bg': 'light green'})

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
