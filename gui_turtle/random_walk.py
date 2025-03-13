import turtle as t
import random

tim=t.Turtle()
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

# color=["red","green","black","wheat"]

direction=[0,90,180,270]
tim.pensize(10)
tim.speed("fastest")

for i in range(200):
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(direction))


screen=t.Screen()
screen.exitonclick()