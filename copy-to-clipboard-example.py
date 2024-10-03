import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tkb

def copy_to_clipboard():
    text = entry.get()

    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Success", "Password copied.")
    else:
        messagebox.showwarning("No text")


root = tkb.Window(themename="darkly")
root.title("Example")

entry = tkb.Entry(root, width=40)
entry.pack(pady=10)

copy_button = tkb.Button(root, text="Copy", command=copy_to_clipboard, bootstyle="success")
copy_button.pack(pady=10)

root.mainloop()
