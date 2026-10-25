number_of_purchased_products = int(input("Enter the number of purchased products: "))
product_price = float(input("Enter the product price: "))

if number_of_purchased_products > 1:
    total_price = product_price + (product_price * 0.75 * (number_of_purchased_products - 1))
else: 
    total_price = product_price

print(f"Amount to pay: {total_price:.2f}")