import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 600)

# Create a turtle
fractal = turtle.Turtle()
fractal.speed(0)
fractal.color("white")

# Generate random fractal pattern
def draw_fractal(length, angle, depth):
    if depth == 0:
        fractal.forward(length)
    else:
        draw_fractal(length * 0.8, -angle, depth - 1)
        fractal.left(angle)
        draw_fractal(length * 0.8, angle, depth - 1)
        fractal.left(angle)
        draw_fractal(length * 0.8, -angle, depth - 1)

# Random parameters
length = random.randint(50, 150)
angle = random.randint(20, 70)
depth = random.randint(3, 6)

# Position the turtle
fractal.penup()
fractal.goto(-100, -100)
fractal.pendown()

# Draw the fractal
draw_fractal(length, angle, depth)

# Hide the turtle and display result
fractal.hideturtle()
turtle.done()
