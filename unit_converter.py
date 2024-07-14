import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def convert():
    try:
        input_value = float(entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")
        return

    if conversion_type.get() == "Length":
        output_value = input_value * 0.621371  # kilometers to miles
    elif conversion_type.get() == "Weight":
        output_value = input_value * 2.20462  # kilograms to pounds
    elif conversion_type.get() == "Temperature":
        output_value = (input_value * 9/5) + 32  # Celsius to Fahrenheit
    else:
        output_value = "Invalid conversion type"

    result_label.config(text=f"Result: {output_value}")

# Create the main window
root = tk.Tk()
root.title("Unit Converter")

# Conversion Type Label
conversion_label = tk.Label(root, text="Select Conversion Type:")
conversion_label.pack(pady=5)

# Conversion Type Combobox
conversion_type = ttk.Combobox(root, values=["Length", "Weight", "Temperature"])
conversion_type.set("Length")
conversion_type.pack(pady=5)

# Input Label
input_label = tk.Label(root, text="Enter Value:")
input_label.pack(pady=5)

# Entry
entry = tk.Entry(root)
entry.pack(pady=5)

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()
