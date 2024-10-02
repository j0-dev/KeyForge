import secrets
import string

import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as tkb
from ttkbootstrap import Style



### MAIN FUNCTION ###

def password():

    lowercase_1 = list(string.ascii_lowercase)
    uppercase_2 = list(string.ascii_uppercase)
    digits_3 = list(string.digits)
    symbols_4 = list(string.punctuation)

    password = ""

    while len(password) < 18:
        list_nums = [1, 2, 3, 4]
        list_pick = secrets.choice(list_nums)

        if list_pick == 1:
            char = secrets.choice(lowercase_1)
            lowercase_1.remove(char)
            password += char

        elif list_pick == 2:
            char = secrets.choice(uppercase_2)
            uppercase_2.remove(char)
            password += char

        elif list_pick == 3:
            char = secrets.choice(digits_3)
            password += char

        else:
            char = secrets.choice(symbols_4)
            symbols_4.remove(char)
            password += char

    
    password_field.config(state="normal")
    password_field.delete(0, tk.END)
    password_field.insert(0, password)
    password_field.config(state="readonly")




### GUI ###

# Main
if __name__ == "__main__":
    root = tk.Tk()
    root.title("KeyForge")

    # Styling
    root.geometry("500x225")
    root.resizable(False, False)
    bg_colour = "#212121"
    fg_colour = "#f3f3f3"
    accent_colour = "#f3f3f3"
    entry_bg_colour = "#212121"
    button_colour = "#00bc8c"
    button_hover_colour = "#00e6ab"

    title_font = tkfont.Font(family="Gadugi", size=30, weight="bold")
    subtitle_font = tkfont.Font(family="Gadugi", size=13)
    main_font = tkfont.Font(family="Gadugi", size=12)
    result_font = tkfont.Font(family="Gadugi", size=16)

    style = tkb.Style()
    style.theme_use("darkly")
    style.configure("TFrame", background=bg_colour)
    style.configure("TLabel", background=bg_colour, foreground=fg_colour, font=main_font)
    style.configure("TEntry", fieldbackground=entry_bg_colour, foreground=fg_colour, font=main_font, borderwidth=1, relief="solid")
    style.configure("Custom.TButton", background=button_colour, foreground=bg_colour, font=main_font, borderwidth=0, focuscolor=button_colour, highlightthickness=0)
    style.map("Custom.TButton", background=[('active', button_hover_colour)], bordercolor=[('focus', button_colour)], highlightcolor=[('focus', button_colour)])

    # Mainframe config
    frame = tkb.Frame(root, padding="10")
    frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
    frame.configure(border=0, relief="flat")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Header
    header_label = tkb.Label(frame, text="KeyForge", font=title_font, anchor="center")
    subtitle_label = tkb.Label(frame, text="Generate strong passwords with a click.", font=subtitle_font, foreground="#9c9c9c")
    header_label.grid(column=0, row=0, columnspan=2, sticky=(tk.W), padx=38, pady=(0, 0))
    subtitle_label.grid(column=0, row=1, columnspan=2, sticky=(tk.W), padx=39, pady=(0, 30))

    # Password gen
    password_field = tkb.Entry(frame, state="readonly", justify="left", font=main_font, width=35)
    password_field.grid(row=2, column=0, sticky=(tk.W), padx=40, pady=(0, 5))
    password_field.configure(takefocus=1)
    password_field.focus_set()

    # Gen button
    generate_button = tkb.Button(frame, text="Generate", command=password, width=10, style="Custom.TButton")
    generate_button.grid(column=0, row=3, pady=(5, 0), padx=40, sticky=(tk.W))

    # Layout
    frame.columnconfigure(1, weight=1)

    # Event loop
    root.configure(bg=bg_colour)
    root.mainloop()
    



    