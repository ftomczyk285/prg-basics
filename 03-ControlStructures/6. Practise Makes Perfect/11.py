previous_product_price = 299.99
current_product_price = 249.99

reduction_percentage = ((previous_product_price - current_product_price) / previous_product_price) * 100

print(f"Current product price is: {current_product_price:.2f}")
print(f"Previous product price was: {previous_product_price:.2f}")
if reduction_percentage >= 10:
    print("Buy the product!")
print(f"Product price reduced by {reduction_percentage:.2f}%")