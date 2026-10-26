import turtle

def draw_square(length):
    # Draw a square
    for i in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(length):
    for i in range(3):
        pen.forward(length)
        pen.right(120)

def draw_rectangle(a, b):
    for i in range(4):
        if i % 2 == 0:
            pen.forward(a)
        else:
            pen.forward(b)
        pen.right(90)

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Draw figures
draw_square(4)
pen.penup()
pen.forward(20)
pen.pendown()

draw_triangle(5)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()






