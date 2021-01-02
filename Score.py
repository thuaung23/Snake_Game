from turtle import Turtle


# Get inheritance from Turtle class.
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Times New Roman", 24, "normal"))

    # Print "game over" when snake collides with a wall.
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=("Times New Roman", 24, "normal"))

    # Add 1 to score everytime snake collides with a food.
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()