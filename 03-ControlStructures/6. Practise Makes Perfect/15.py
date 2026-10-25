EAN = input("Enter the EAN-13 article number: ")

if len(EAN) != 13 or not EAN.isdigit():
    print("Invalid EAN-13 number. Please enter a 13-digit number.")
else:
    print("Article number is correct.")
    country_code = EAN[:3]
    if country_code == "590":
        print("Article manufactured in Poland.")