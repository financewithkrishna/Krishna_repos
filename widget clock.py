import tkinter as tk
from math import cos, sin, pi
from time import localtime

def update_clock():
    current_time = localtime()
    hour = current_time.tm_hour % 12
    minute = current_time.tm_min
    second = current_time.tm_sec

    hour_angle = (hour * 30) + (minute / 2)
    minute_angle = minute * 6
    second_angle = second * 6

    draw_clock(hour_angle, minute_angle, second_angle)

    # Update the clock every 1000 milliseconds (1 second)
    window.after(1000, update_clock)

def draw_clock(hour_angle, minute_angle, second_angle):
    # Clear previous drawings
    canvas.delete("all")

    # Clock face
    canvas.create_oval(50, 50, 250, 250, outline="black", width=2)

    # Draw clock numbers
    for i in range(1, 13):
        angle = pi / 6 * (i - 3)
        x = 150 + 90 * cos(angle)
        y = 150 + 90 * sin(angle)
        canvas.create_text(x, y, text=str(i), font=("Arial", 12))

    # Hour hand
    hour_hand_length = 50
    hour_x = 150 + hour_hand_length * sin(pi * hour_angle / 180)
    hour_y = 150 - hour_hand_length * cos(pi * hour_angle / 180)
    canvas.create_line(150, 150, hour_x, hour_y, fill="black", width=4)

    # Minute hand
    minute_hand_length = 70
    minute_x = 150 + minute_hand_length * sin(pi * minute_angle / 180)
    minute_y = 150 - minute_hand_length * cos(pi * minute_angle / 180)
    canvas.create_line(150, 150, minute_x, minute_y, fill="black", width=3)

    # Second hand
    second_hand_length = 80
    second_x = 150 + second_hand_length * sin(pi * second_angle / 180)
    second_y = 150 - second_hand_length * cos(pi * second_angle / 180)
    canvas.create_line(150, 150, second_x, second_y, fill="red", width=2)

# Create the main window
window = tk.Tk()
window.title("Analog Clock")

# Create a canvas for drawing the clock
canvas = tk.Canvas(window, width=300, height=300, bg="white")
canvas.pack()

# Call the update_clock function to start the clock
update_clock()

# Run the main event loop
window.mainloop()
