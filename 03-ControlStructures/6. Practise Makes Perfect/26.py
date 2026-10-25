PIN = "0805"
remaining_attempts = 3
while remaining_attempts >= 0:
    if remaining_attempts == 0:
            print("Sorry, your payment card has been blocked.")
    else:
        entered_pin = input("Enter the PIN code: ")
        if entered_pin == PIN:
            print("Access granted.")
            break
        else:
            remaining_attempts -= 1
            print(f"Incorrect...")
    