###
# A Program that checks whether a given number i positive, negative or zero. 
# The program should print the appropriate message.
#

number = int(input('Enter a number: '))

if number > 0:
    print(f'{number} is a positive number')
elif number < 0:
    print(f'{number} is a negative number')
else:
    print(f'{number} is zero')