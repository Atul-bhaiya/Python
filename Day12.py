# Mini Task – Temperature Converter (using module import)
# main.py

from temp_converter import celsius_to_fahrenheit, fahrenheit_to_celsius

print("== Temperature Converter ==")
choice = input("Type 'C' to convert to Celsius, 'F' to convert to Fahrenheit: ").upper()

if choice == 'C':
    f = float(input("Enter temperature in Fahrenheit: "))
    c = fahrenheit_to_celsius(f)
    print(f"{f}°F = {round(c, 2)}°C")

elif choice == 'F':
    c = float(input("Enter temperature in Celsius: "))
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C = {round(f, 2)}°F")

else:
    print("Invalid choice!")
