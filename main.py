from turtle import Turtle, Screen
from snake import Snake
import random
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")

score = 0

snake = Snake()
scoreboard = Scoreboard()
food = Food()

screen.tracer(0)

game_is_on = True
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while game_is_on:

    sX = snake.head.xcor()
    sY = snake.head.ycor()
    snake.move()

    screen.update()
    time.sleep(0.1)

# detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.updateScore()

    if sX> 280 or sX < - 280 or sY> 280 or sY < - 280 :
        scoreboard.endGame()
        game_is_on = False

    for p in snake.ps:
        if p == snake.head:
            pass
        elif snake.head.distance(p) < 10:
            game_is_on = False
            scoreboard.endGame()





screen.exitonclick()