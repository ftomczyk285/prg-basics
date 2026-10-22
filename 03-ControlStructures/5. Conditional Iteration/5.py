###
# Sums numbers entered by user
#
total_sum = 0
numbers_entered = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    numbers_entered += 1

    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number

print(f"The total sum of the numbers is: {total_sum}")

arithmetic_mean = total_sum / (numbers_entered - 1)  # Subtract 1 to exclude the terminating 0
print(f"The arithmetic mean of the numbers is: {arithmetic_mean}")