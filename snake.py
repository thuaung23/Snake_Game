from turtle import Turtle

# It is important to have the correct coordinates. (x, y)
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __int__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in START_POSITIONS:
            jack = Turtle(shape="square")
            jack.color("black")
            jack.penup()
            jack.goto(position)
            self.snake_body.append(jack)

    def move_the_snake(self):
        for body_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_num - 1].xcor()
            new_y = self.snake_body[body_num - 1].ycor()
            self.snake_body[body_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
