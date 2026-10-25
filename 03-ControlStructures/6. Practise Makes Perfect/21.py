amount = int(input("Enter the amount in PLN: "))
print(f"The amount of PLN {amount} in coins:")
if amount >= 5:
    coins_5 = amount // 5
    amount %= 5
    print(f"5 PLN coins: {coins_5}")
if amount >= 2:
    coins_2 = amount // 2
    amount %= 2
    print(f"2 PLN coins: {coins_2}")
if amount >= 1:
    coins_1 = amount
    print(f"1 PLN coins: {coins_1}")