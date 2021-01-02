from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("black")
        self.speed("fastest")

    def create_new_food(self):
        rand_xcor = random.randint(-285, 285)
        rand_ycor = random.randint(-285, 285)
        self.goto(rand_xcor, rand_ycor)