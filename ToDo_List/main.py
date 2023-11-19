import tkinter as tk
from tkinter import ttk


def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()


def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
        save_tasks()


def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
            for task in tasks:
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass


window = tk.Tk()
window.title("To-Do List")
window.geometry("400x400")
window.configure(bg="gold")
# Create a label at the top with "Consolas" font
label = tk.Label(window, text="ToDo List", bg="gold", font=("Consolas", 20))
label.pack(pady=10)

listbox = tk.Listbox(window, selectmode=tk.SINGLE, width=40, height=10, bg="lightyellow",
                     highlightthickness=0)
listbox.pack()

entry = tk.Entry(window, width=40, bg="lightyellow", highlightthickness=0)
entry.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack(side=tk.BOTTOM, pady=10)

add_button = ttk.Button(button_frame, text="Add Task", command=add_task, style='Round.TButton')
add_button.pack(side=tk.LEFT)

remove_button = ttk.Button(button_frame, text="Remove Task", command=remove_task, style='Round.TButton')
remove_button.pack(side=tk.LEFT)

load_tasks()

window.mainloop()

