import tkinter as tk
from tkinter import ttk


def toggle_theme():
    current_theme = window.tk.call('ttk::style', 'theme', 'use')
    if current_theme == 'clam':
        window.tk.call('ttk::style', 'theme', 'winnative')
    else:
        window.tk.call('ttk::style', 'theme', 'clam')


window = tk.Tk()
window.title("Dark Mode and Light Mode")
window.geometry('400x300')

style = ttk.Style()
style.theme_create("light", settings={
    ".": {
        "configure": {
            "background": '#FFFFFF',  # Set a light background color
            "foreground": '#000000',  # Set the text color
        }
    },
    "TLabel": {
        "configure": {
            "background": '#FFFFFF',  # Set a light background color for labels
            "foreground": '#000000',  # Set the text color for labels
        }
    },
    "TButton": {
        "configure": {
            "background": '#FFFFFF',  # Set the button background color in light mode
            "foreground": '#000000',  # Set the button text color in light mode
        }
    }
})

style.theme_create("dark", settings={
    ".": {
        "configure": {
            "background": '#222222',  # Set a dark background color
            "foreground": '#FFFFFF',  # Set the text color
        }
    },
    "TLabel": {
        "configure": {
            "background": '#222222',  # Set a dark background color for labels
            "foreground": '#FFFFFF',  # Set the text color for labels
        }
    },
    "TButton": {
        "configure": {
            "background": '#222222',  # Set the button background color in dark mode
            "foreground": '#FFFFFF',  # Set the button text color in dark mode
        }
    }
})

style.theme_use("light")

toggle_button = ttk.Button(window, text="Toggle Theme", command=toggle_theme)
toggle_button.pack(pady=10)

label = ttk.Label(window, text="This is a Python GUI with dark and light mode")
label.pack(pady=50)


window.mainloop()
