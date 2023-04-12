from turtle import Turtle,Screen
x = 0
y = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake")

starting_positions = [(0,0),(-20,0),(-40,0)]
segment = Turtle("square")
segment.color("white")
snake_length = 2

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)


# segment_1 = Turtle("square")
# segment_1.color("white")
# segment_1.setpos( x = x, y = y)
#
# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.setpos( x = x+20, y = y)
#
# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.setpos( x = x+40, y = y)














screen.exitonclick()
