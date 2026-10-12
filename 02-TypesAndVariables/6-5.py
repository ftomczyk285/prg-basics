###
# A program that prints 9-digit telephone number as three groups
# of 3 digits each
#
number = input("Enter phone number: ")
separated = number[:3] + '-' + number[3:6] + '-' + number[6:]
print(f"Phone number: {separated}")