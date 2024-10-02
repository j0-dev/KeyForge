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

    
    return password




### GUI ###

# Main
if __name__ == "__main__":
    root = tk.Tk()
    root.title("KeyForge")

    # Styling
    root.geometry("650x225")
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

# Event loop
root.configure(bg=bg_colour)
root.mainloop()
    



    