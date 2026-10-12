###
# Calculation of circle area and circumference 
#
import math
radius = int(input("Enter radius: "))
area = math.pi * radius**2
circumference = 2 * math.pi * radius
print(f'Circle\'s radius: {radius}')
print(f'Circle\'s area: {area}')
print(f'Circle\'s circumference: {circumference}')