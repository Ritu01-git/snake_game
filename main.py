from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=500, height=500)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
race_is_on = True

while race_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.all_segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.all_segments[0].xcor() > 250 or snake.all_segments[0].xcor() < -250 or snake.all_segments[
        0].ycor() > 250 or snake.all_segments[0].ycor() < -250:
        race_is_on = False
        score.game_over()

    for segment in snake.all_segments[1:]:

        if snake.all_segments[0].distance(segment) < 10:
            race_is_on = False
            score.game_over()

screen.exitonclick()