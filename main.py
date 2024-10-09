import turtle
from turtle import Turtle, Screen
import random
# from module import class

tim = Turtle()



turtle.colormode(255)
# colors = ["red", "blue", "green", "yellow", "pink", "black","orange","brown"]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270,]
tim.pensize(15)
tim.speed("fastest")
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))



























# def draw_shapes(i):
#     angle = 360 / i
#     for _ in range(i):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3,11) :
#     tim.color(random.choice(colors))
#     draw_shapes(shape_side_n)


    # i += 1
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)


screen = Screen()
screen.exitonclick()