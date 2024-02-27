import tkinter as tk
from tkinter import messagebox

# Function to handle the settings button event
def show_settings():
    messagebox.showinfo("Settings", "Choose mode:")

# Function to handle the light mode switch
def switch_to_light():
    # Implement your logic to switch to light mode here
    print("Switching to light mode")

# Function to handle the dark mode switch
def switch_to_dark():
    # Implement your logic to switch to dark mode here
    print("Switching to dark mode")

# Create the main window
window = tk.Tk()

# Create a settings button
settings_button = tk.Button(window, text="Settings", command=show_settings)
settings_button.pack()

# Create the light mode switch
light_mode_button = tk.Button(window, text="Light Mode", command=switch_to_light)
light_mode_button.pack()

# Create the dark mode switch
dark_mode_button = tk.Button(window, text="Dark Mode", command=switch_to_dark)
dark_mode_button.pack()

# Start the GUI event loop
window.mainloop()

