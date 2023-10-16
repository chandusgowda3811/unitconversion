import tkinter as tk

# Conversion functions
def perform_conversion():
    value_str = entry_value.get()
    conversion_type = conversion_var.get()
    specific_conversion = specific_conversion_var.get()

    # Check if a conversion type is selected
    if not conversion_type:
        result_label.config(text="Select Conversion Type")
        return

    # Check if a specific conversion option is selected
    if not specific_conversion:
        result_label.config(text="Select Specific Conversion")
        return

    # Check if a valid numeric value is provided
    if not value_str:
        result_label.config(text="Enter a Value")
        return

    try:
        value = float(value_str)
    except ValueError:
        result_label.config(text="Invalid Input")
        return

    if conversion_type == "Length":
        result = perform_length_conversion(value, specific_conversion)
    elif conversion_type == "Mass":
        result = perform_mass_conversion(value, specific_conversion)
    elif conversion_type == "Temperature":
        result = perform_temperature_conversion(value, specific_conversion)
    elif conversion_type == "Time":
        result = perform_time_conversion(value, specific_conversion)
    elif conversion_type == "Speed":
        result = perform_speed_conversion(value, specific_conversion)
    elif conversion_type == "Energy":
        result = perform_energy_conversion(value, specific_conversion)
    elif conversion_type == "Pressure":
        result = perform_pressure_conversion(value, specific_conversion)
    else:
        result = "Invalid Conversion"

    result_label.config(text=result)


# Conversion functions for specific conversion options
def perform_length_conversion(value, specific_conversion):
    if specific_conversion == "Centimeter to Meter":
        return value / 100
    elif specific_conversion == "Meter to Centimeter":
        return value * 100
    elif specific_conversion == "Centimeter to Inch":
        return value / 2.54
    elif specific_conversion == "Inch to Centimeter":
        return value * 2.54
    return "Invalid Conversion"

def perform_mass_conversion(value, specific_conversion):
    if specific_conversion == "Gram to Kilogram":
        return value / 1000
    elif specific_conversion == "Kilogram to Gram":
        return value * 1000
    return "Invalid Conversion"

def perform_temperature_conversion(value, specific_conversion):
    if specific_conversion == "Celsius to Fahrenheit":
        return (value * 9/5) + 32
    elif specific_conversion == "Fahrenheit to Celsius":
        return (value - 32) * 5/9
    return "Invalid Conversion"

def perform_time_conversion(value, specific_conversion):
    if specific_conversion == "Second to Minute":
        return value / 60
    elif specific_conversion == "Minute to Second":
        return value * 60
    return "Invalid Conversion"

def perform_speed_conversion(value, specific_conversion):
    if specific_conversion == "Miles per Hour to Kilometers per Hour":
        return value * 1.60934
    elif specific_conversion == "Kilometers per Hour to Miles per Hour":
        return value / 1.60934
    return "Invalid Conversion"

def perform_energy_conversion(value, specific_conversion):
    if specific_conversion == "Joule to Kilojoule":
        return value / 1000
    elif specific_conversion == "Kilojoule to Joule":
        return value * 1000
    return "Invalid Conversion"

def perform_pressure_conversion(value, specific_conversion):
    if specific_conversion == "Bar to Pascal":
        return value * 100000
    elif specific_conversion == "Pascal to Bar":
        return value / 100000
    return "Invalid Conversion"

# Create the main window
window = tk.Tk()
window.title("Unit Conversion")
window.geometry("600x360")  # Set the window size

# Create a label for the title
title_label = tk.Label(window, text="Unit Conversion", font=("Arial", 18),bg="lightgreen")
title_label.pack(pady=10)

# Create a frame to hold the widgets for better alignment
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

# Create a label for selecting the type of conversion
conversion_label = tk.Label(input_frame, text="Select Type of Conversion", font=("Arial", 14),bg="lightgreen")
conversion_label.grid(row=0, column=0, padx=10, pady=5)

conversion_var = tk.StringVar(window)
conversion_options = ["Length", "Mass", "Temperature", "Time", "Speed", "Energy", "Pressure"]
custom_font = ("Helvetica", 16)  
conversion_menu = tk.OptionMenu(input_frame, conversion_var, *conversion_options)
conversion_menu.config(font=custom_font, width=20)  
conversion_menu.grid(row=0, column=1, padx=10, pady=5)

# Create a label for selecting the specific conversion option
specific_conversion_label = tk.Label(input_frame, text="Select Specific Conversion", font=("Arial", 14),bg="lightgreen")
specific_conversion_label.grid(row=1, column=0, padx=10, pady=5)

# Dropdown menu to select specific conversion
specific_conversion_var = tk.StringVar(window)
specific_conversion_menu = tk.OptionMenu(input_frame, specific_conversion_var, "")
specific_conversion_menu.config(font=custom_font,width=20)
specific_conversion_menu.grid(row=1, column=1, padx=10, pady=5)

# Entry field for value input
value_label = tk.Label(input_frame, text="Enter Value", font=("Arial", 14),bg="lightblue",width=20)
value_label.grid(row=2, column=0, padx=10, pady=5)

entry_value = tk.Entry(input_frame, font=("Arial", 19))
entry_value.grid(row=2, column=1, padx=10, pady=5)

# Button to perform the conversion
convert_button = tk.Button(window, text="Convert", font=("Arial", 18), command=perform_conversion, bg="blue", fg="white")
convert_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 18), relief="solid", borderwidth=1, width=20, height=1)
result_label.pack(pady=10)

# Function to update specific conversion options
def update_specific_conversion_menu(*args):
    specific_conversion_options = get_specific_conversions(conversion_var.get())
    specific_conversion_var.set("")  # Reset selection
    specific_conversion_menu['menu'].delete(0, 'end')  # Clear previous options
    for option in specific_conversion_options:
        specific_conversion_menu['menu'].add_command(label=option, command=tk._setit(specific_conversion_var, option))

# Dictionary to store specific conversion options
specific_conversions = {
    "Length": ["Centimeter to Meter", "Meter to Centimeter", "Centimeter to Inch", "Inch to Centimeter"],
    "Mass": ["Gram to Kilogram", "Kilogram to Gram"],
    "Temperature": ["Celsius to Fahrenheit", "Fahrenheit to Celsius"],
    "Time": ["Second to Minute", "Minute to Second"],
    "Speed": ["Miles per Hour to Kilometers per Hour", "Kilometers per Hour to Miles per Hour"],
    "Energy": ["Joule to Kilojoule", "Kilojoule to Joule"],
    "Pressure": ["Bar to Pascal", "Pascal to Bar"]
}

# Function to get specific conversion options based on the selected conversion type
def get_specific_conversions(conversion_type):
    return specific_conversions.get(conversion_type, [])

conversion_var.trace("w", update_specific_conversion_menu)

# Start the GUI main loop
window.mainloop()
