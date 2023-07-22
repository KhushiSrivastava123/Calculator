import tkinter as tk
from tkinter import ttk
import math

def on_click(event):
    current_text = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "√":
        try:
            result = math.sqrt(eval(current_text))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "x^2":
        try:
            result = eval(current_text) ** 2
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "⌫":
        entry.delete(len(current_text) - 1, tk.END)
    else:
        entry.insert(tk.END, text)

# Function to change button color on press
def animate_button_press(widget):
    original_color = widget.cget("background")
    widget.configure(background="#ff8000")  # Change to your preferred color
    widget.after(150, lambda: widget.configure(background=original_color))

# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

# Entry widget to display the expression/result
entry = ttk.Entry(root, font=("Helvetica", 20), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Define the buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("⌫", 5, 1), ("√", 5, 2), ("x^2", 5, 3),
]

# Create the buttons and bind their actions
for (text, row, col) in buttons:
    button = ttk.Button(root, text=text, style="C.TButton")
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", lambda event, widget=button: (on_click(event), animate_button_press(widget)))

# Apply custom style for the buttons
style = ttk.Style()
style.configure("C.TButton", background="#ffcc66", foreground="black", relief="flat", borderwidth=0, font=("Helvetica", 20))

# Adjust row and column weights so that the buttons expand with the window
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
