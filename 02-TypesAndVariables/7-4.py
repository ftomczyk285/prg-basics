###
# A program that checks if a tree meets conditions to be cut down
#
import math
circumference = int(input("Enter tree circumference in cm: "))
diameter = circumference / math.pi
can_be_cut_down = diameter >= 50
print("Tree can be cut down:", can_be_cut_down)