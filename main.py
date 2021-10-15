# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
# print(timmy)
# print(timmy.position())
# timmy.shape("turtle")
# timmy.color("LightSeaGreen")
# timmy.forward(100)
# print(timmy.position())
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table.align)
print(table)