from turtle import Screen
from Snake import Snake
from Food import Food
from Score import Score
import time

# Create a fixed size screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


# Direct the snake by pressing specific keys on keyboard.
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_on = True
while game_on:
    screen.update()
    # To move snake slower.
    time.sleep(.2)
    snake.move_the_snake()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.create_new_food()
        snake.extend()
        score.add_score()

    # Check if the head of the snake collides with walls.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    # Check if snake head collides with tail.
    for block in snake.snake_body[1:]:
        if snake.head.distance(block) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()
