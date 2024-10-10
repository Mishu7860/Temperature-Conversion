def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature():
    # Get temperature value from user
    temperature = float(input("Enter the temperature value: "))
    
    # Get unit of measurement from user
    unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit == 'C':
        # Convert from Celsius to Fahrenheit
        converted_temp = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
    
    elif unit == 'F':
        # Convert from Fahrenheit to Celsius
        converted_temp = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
    
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Example usage:
convert_temperature()
