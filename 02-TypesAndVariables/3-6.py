###
# A program that calculates and prints the distance to the horizon 
# depending on on the height of the observer
#
import math
h = float(input("Enter observer's height in meters: "))
d = 3.57 * math.sqrt(h)
# d = round(d, 2)
print(f"Observer's distance to the horizon is {d} kilometers")