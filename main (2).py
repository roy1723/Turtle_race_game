import random
from turtle import Turtle, Screen
from random import Random
is_race_on = False
screen = Screen()
screen.setup(width= 500, height=400)
user_bet =screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [ -60, -20, 20, 60, 100, 140]
all_turtle= []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-490, y = y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print("Hooray! Your turtle won!")
            else:
                print(f"{winning_color} is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()


