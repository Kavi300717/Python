#Function to convert Fahrenheit to Celsious
def fahrenheit_celsious(fahrenheit):
    celsius = (fahrenheit - 32 )* 5 / 9
    return celsius

def celsius_fahrenheit(celsius):
    fahrenheit = (celsius * 9 /5) +32
    return fahrenheit

temperature = float(input("Enter temperature: "))

conversion_type = input("Select a conversion type(1 for Fahrenheit to Celsius, 2 for Celsius to Fahrenheit): ")

if conversion_type == '1':
    converted_temperature = fahrenheit_to_celsius(temperature)
    print(f"Converted temperature : {converted_temperature:.1f}°C")
elif conversion_type == '2':
    converted_temperature = celsius_to_fahrenheit(temperature)
    print(f"Comverted temperature: {converted_temperature:.1f}°F")
else:
    print("Invalid selection. Please choose 1 or 2.")