from turtle import Turtle, Screen
import random



screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

is_race_on = False

all_turtles = []
start_y = -100

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.fillcolor(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_y)
    start_y += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        
        if turtle.xcor() >220:
            is_race_on = False
            winning_color = turtle.fillcolor()
            message_turtle = Turtle()
            message_turtle.hideturtle()
            message_turtle.penup()
            message_turtle.goto(0, 0)
            message_turtle.pencolor(winning_color)
            if winning_color == user_bet:
                message_turtle.write(f"You've won! The {winning_color} turtle is the winner!", align="center", font=("Arial", 16, "normal"))
            else:
                message_turtle.write(f"You've lost! The {winning_color} turtle is the winner!", align="center", font=("Arial", 16, "normal"))
            
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)
























screen.exitonclick()


