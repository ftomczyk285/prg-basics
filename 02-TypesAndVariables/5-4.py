###
# A program that reads the amount and calculates it's VAT
#
amount = round(float(input("Enter an ammount: ")), 2)
vat = round(0.23 * amount, 2)
print(f"Amount: {amount}")
print(f"VAT: {vat}")