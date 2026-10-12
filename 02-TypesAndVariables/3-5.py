###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2)
# diagonal = round(diagonal, 2)
print(f"The diagonal of a rectangle with sides a = {a} and b = {b} is {diagonal}")