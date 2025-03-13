# import turtle
# from turtle import Turtle , Screen
# tony=Turtle()
# print(tony)
#
# tony.shape("turtle")
# tony.color("green")
# tony.forward(100)
# my_screen= Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Pokemon",["Pikachu","Squirtle","Charmendar"])
table.add_column("Type",["Electric","Water","Fire"])
table.align ="l"
print(table)

