import tkinter as tk

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operator.get()

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            result = "Cannot divide by zero!"
        else:
            result = num1 / num2

    result_label.config(text="Result: " + str(result))

# Create a tkinter window
window = tk.Tk()
window.title("Calculator")

# Create entry fields and labels
entry1 = tk.Entry(window)
entry1.grid(row=0, column=0)

operator = tk.StringVar(window)
operator.set('+')
operator_dropdown = tk.OptionMenu(window, operator, '+', '-', '*', '/')
operator_dropdown.grid(row=0, column=1)

entry2 = tk.Entry(window)
entry2.grid(row=0, column=2)

calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=1, columnspan=3)

result_label = tk.Label(window, text="")
result_label.grid(row=2, columnspan=3)

# Start the GUI event loop
window.mainloop()
