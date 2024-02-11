import tkinter as tk
from tkinter import ttk

def on_click(char):
    current_text = display_var.get()
    display_var.set(current_text + char)

def calculate(event=None):
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except Exception as e:
        display_var.set("Error")

def clear():
    display_var.set("")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create a variable to store the display text
display_var = tk.StringVar()
display_var.set("")

# Create the display entry field
display_entry = tk.Entry(window, textvariable=display_var, justify="right", font=("Arial", 18))
display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create buttons for each number and operation
row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(window, text=button, width=8, height=2, command=calculate).grid(row=row, column=col)
    elif button == '0':
        tk.Button(window, text=button, width=8, height=2, command=lambda b=button: on_click(b)).grid(row=row, column=col, columnspan=2)
        col += 1
    else:
        tk.Button(window, text=button, width=4, height=2, command=lambda b=button: on_click(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create a Clear button
tk.Button(window, text="Clear", width=4, height=2, command=clear).grid(row=row, column=0, columnspan=2)

# Bind the Enter key to the calculate function
window.bind('<Return>', calculate)

# Run the main event loop
window.mainloop()

