from turtle import Turtle

# It is important to have the correct coordinates. (x, y)
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # Create empty list to make the body of snake.
        self.snake_body = []
        # Call function to crate a snake.
        self.create_snake()
        # Set first item in the created list to be the head of the snake.
        self.head = self.snake_body[0]

    def create_snake(self):
        # Make snake body by placing 3 blocks of squares at different starting positions.
        for position in START_POSITIONS:
            self.add_snake_body(position)

    # Create 3 blocks of squares.
    def add_snake_body(self, position):
        jack = Turtle(shape="square")
        jack.color("black")
        jack.penup()
        jack.goto(position)
        self.snake_body.append(jack)

    # Move blocks one spot ahead starting from last position.
    def move_the_snake(self):
        for body_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_num - 1].xcor()
            new_y = self.snake_body[body_num - 1].ycor()
            self.snake_body[body_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Add one block to snake body when it collides with a food.
    def extend(self):
        self.add_snake_body(self.snake_body[-1].position())

    def move_up(self):
        # Snake isn't allowed to move up while heading downward or switching head and tail.
        if self.head.heading() != DOWN:
            # Change direction to 90 degree.
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            # Change direction to 270 degree.
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            # Change direction to 180 degree.
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            # Change direction to 0 or 360 degree.
            self.head.setheading(RIGHT)
