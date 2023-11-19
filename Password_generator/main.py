import tkinter as tk
from tkinter import ttk
import random
import string


def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special):

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = ""
    if use_lowercase:
        all_characters += lowercase_letters
    if use_uppercase:
        all_characters += uppercase_letters
    if use_digits:
        all_characters += digits
    if use_special:
        all_characters += special_characters


    if length < 8 or not all_characters:
        return "Password length must be at least 8 characters, and at least one character set must be selected."


    # Generate the password
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password


def generate_button_clicked():
    length = length_var.get()
    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special)
    result_var.set(password)


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    root.update()



root = tk.Tk()
root.title("Password Generator")

result_var = tk.StringVar()

length_label = ttk.Label(root, text="Password Length:")
length_var = tk.IntVar(value=12)
length_entry = ttk.Entry(root, textvariable=length_var)

lowercase_var = tk.BooleanVar(value=True)
lowercase_check = ttk.Checkbutton(root, text="Lowercase", variable=lowercase_var)

uppercase_var = tk.BooleanVar(value=True)
uppercase_check = ttk.Checkbutton(root, text="Uppercase", variable=uppercase_var)

digits_var = tk.BooleanVar(value=True)
digits_check = ttk.Checkbutton(root, text="Digits", variable=digits_var)

special_var = tk.BooleanVar(value=True)
special_check = ttk.Checkbutton(root, text="Special Characters", variable=special_var)

generate_button = ttk.Button(root, text="Generate Password", command=generate_button_clicked)
copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)

result_label = ttk.Label(root, textvariable=result_var)


length_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
length_entry.grid(row=0, column=1, padx=10, pady=5)
lowercase_check.grid(row=1, column=0, sticky="w", padx=10, pady=5)
uppercase_check.grid(row=1, column=1, sticky="w", padx=10, pady=5)
digits_check.grid(row=2, column=0, sticky="w", padx=10, pady=5)
special_check.grid(row=2, column=1, sticky="w", padx=10, pady=5)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)
copy_button.grid(row=4, column=0, columnspan=2, pady=5)
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()

