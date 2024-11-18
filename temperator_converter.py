# formula for temperature convert
#celcius to fahrenheit
# (0°C × 9/5) + 32 = 32°F
# fahrenheit to celcius
# (0°F − 32) × 5/9 = -17.78°C

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    # Ask user to choose the conversion type
    while True:
        choice = input("Type 'C' to convert Celsius to Fahrenheit, or 'F' to convert Fahrenheit to Celsius: ").strip().upper()

        if choice not in ['C', 'F']:
            print("Invalid choice! Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            continue
        else:
            break

    # Ask for temperature and validate input
    while True:
        temp_input = input("Enter the temperature value: ").strip()
        try:
            temperature = float(temp_input)
            break
        except ValueError:
            print("Invalid temperature! Please enter a valid number.")

    # Perform conversion based on the user's choice
    if choice == 'C':
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {result}°F")
    else:
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is equal to {result}°C")

# Run the converter
if __name__ == "__main__":   # chatgpt prompt for this
    temperature_converter()

    
    
# help me to understand what is this , why u used and if i miss something also give in input

# ChatGPT said:
# ChatGPT
# Let me explain the line you're asking about, as well as the purpose of the entire structure:

# The Line: if __name__ == "__main__":
# This is a common Python construct that checks whether a script is being run directly or imported as a module into another script.

# Detailed Breakdown:
# __name__: Every Python module (file) has a special built-in variable called __name__.
# If the script is run directly (like python script.py), then __name__ will be set to "__main__".
# If the script is imported as a module in another script, __name__ will be set to the module’s name (the filename without .py).
# if __name__ == "__main__":
# This line checks if the script is being executed directly.
# If True, the code under this condition will run.
# If False (meaning it's being imported elsewhere), that code won’t run.
# Why Use It?
# It’s useful when:

# You want some code (e.g., running the main function) to execute only when the script is run directly, not when it is imported.
# It helps to separate script execution from module behavior. You can use the same file as both a script and a module.
# In Your Code:
# python
# Copy code
# if __name__ == "__main__":
#     temperature_converter()
# This ensures that the temperature_converter() function is called only when you run this script directly, but not when you import this file elsewhere.

# How the Script Works:
# The script defines the functions and logic first.
# Then, it checks if __name__ == "__main__": at the bottom to only run the temperature_converter() function if the script is executed directly.
# If you remove this, the temperature_converter() function would run whenever the file is loaded, even if it's imported by another Python file, which might not be desirable.

# Input Example:
# Here’s an example of what user input and output would look like when you run this script:

# Input 1: Convert Celsius to Fahrenheit
# bash
# Copy code
# $ python temp_converter.py
# Type 'C' to convert Celsius to Fahrenheit, or 'F' to convert Fahrenheit to Celsius: C
# Enter the temperature value: 25
# Output:
# vbnet
# Copy code
# 25°C is equal to 77.00°F
# Input 2: Convert Fahrenheit to Celsius
# bash
# Copy code
# $ python temp_converter.py
# Type 'C' to convert Celsius to Fahrenheit, or 'F' to convert Fahrenheit to Celsius: F
# Enter the temperature value: 77
# Output:
# vbnet
# Copy code
# 77°F is equal to 25.00°C
# Summary:
# The if __name__ == "__main__": block ensures the script runs only when executed directly.
# Without it, your function would run even when the file is imported elsewhere, which is often not what you want.
# This construct allows your code to be more modular and reusable.