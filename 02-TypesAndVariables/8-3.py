###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# Read temperature from keyboard
celsius = float(input("Enter the temperature in degrees Celsius: "))
# Convert it to Kelvin
kelvin = celsius + 273.15
# Convert it to Fahrenheit
fahrenheit = celsius * 1.8 + 32
# Print the results
print(f'{celsius} degrees Celsius is {kelvin} Kelvins and {fahrenheit} degrees Fahrenheit')