###
# A program that simulates a parking meter
#

number_of_parking_hours = int(input('Enter number of parking hours: '))

parking_fee = 0

if number_of_parking_hours >= 1 and number_of_parking_hours <= 2:
    parking_fee = 5
elif number_of_parking_hours >= 3 and number_of_parking_hours <= 6:
    parking_fee = 15
elif number_of_parking_hours > 6:
    parking_fee = 20

print(f'Parking fee is {parking_fee} PLN')