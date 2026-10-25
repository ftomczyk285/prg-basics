dec = int(input("Enter a natural number: "))

bin = ""

while dec > 0:
    r = dec % 2
    bin = str(r) + bin
    dec //= 2

print(f"The binary representation of the entered number is: {bin}")