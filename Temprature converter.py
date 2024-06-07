from tkinter import *
import tkinter as tk

def convert_temperature():
    try:
        temperature = float(entry_temperature.get())
        original_unit = combo_original_unit.get()
        
        if original_unit == "Celsius":
            converted_fahrenheit = (temperature * 9/5) + 32
            converted_kelvin = temperature + 273.15
            
            label_result.config(text=f"Fahrenheit: {converted_fahrenheit:.2f}\nKelvin: {converted_kelvin:.2f}")
        elif original_unit == "Fahrenheit":
            converted_celsius = (temperature - 32) * 5/9
            converted_kelvin = (temperature + 459.67) * 5/9

            label_result.config(text=f"Celsius: {converted_celsius:.2f}\nKelvin: {converted_kelvin:.2f}")
        else:  # Kelvin
            converted_celsius = temperature - 273.15
            converted_fahrenheit = (temperature * 9/5) - 459.67
        
        label_result.config(text=f"Celsius: {converted_celsius:.2f}\nFahrenheit: {converted_fahrenheit:.2f}")
    except ValueError:
        label_result.config(text="Please enter a valid temperature value.")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Create temperature entry widget
entry_temperature = tk.Entry(window)
entry_temperature.pack()

# Create dropdown menu for original unit
original_units = ["Celsius", "Fahrenheit", "Kelvin"]
combo_original_unit = tk.StringVar(window)
combo_original_unit.set(original_units[0])  # default value
dropdown_original_unit = tk.OptionMenu(window, combo_original_unit, *original_units)
dropdown_original_unit.pack()

# Create button to convert temperature
convert_button = tk.Button(window, text="Convert", command=convert_temperature)
convert_button.pack()

# Create label to display result
label_result = tk.Label(window, text="")
label_result.pack()


# Run the main loop
window.mainloop()
