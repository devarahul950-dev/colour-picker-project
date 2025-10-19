import tkinter as tk
from tkinter import colorchooser

# Function to pick a color
def pick_color():
    color = colorchooser.askcolor(title="Choose a color")
    if color[1]:  # if user picked a color
        rgb_label.config(text=f"RGB: {color[0]}")
        hex_label.config(text=f"HEX: {color[1]}")
        color_box.config(bg=color[1])

# Create window
root = tk.Tk()
root.title("Color Picker")

# Button to pick color
btn = tk.Button(root, text="Pick a Color", command=pick_color)
btn.pack(pady=10)

# Labels to show RGB and HEX values
rgb_label = tk.Label(root, text="RGB:")
rgb_label.pack()
hex_label = tk.Label(root, text="HEX:")
hex_label.pack()

# Box to display the chosen color
color_box = tk.Label(root, bg="white", width=20, height=2)
color_box.pack(pady=10)

# Run the app
root.mainloop()

