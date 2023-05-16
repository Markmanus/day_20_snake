from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake")
screen.tracer(0)

my_snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(my_snake.up,"Up")
screen.onkey(my_snake.down,"Down")
screen.onkey(my_snake.left,"Left")
screen.onkey(my_snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    #detect collision with food
    if my_snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()


# starting_positions = [(0,0),(-20,0),(-40,0)]
#
#
# segments = []
#
# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
#     print(new_segment)
#
#
#
#
#







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
