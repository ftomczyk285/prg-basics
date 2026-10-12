###
# A program that converts a decimal number to binary and hexadecimal
#
decimal = int(input("Enter any number: "))
binary = bin(decimal)
hexadecimal = hex(decimal)
print(f'Binary: {binary}')
print(f'Hexadecimal: {hexadecimal}')