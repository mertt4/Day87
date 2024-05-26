from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("artwork/paddle.gif")
        self.penup()
        self.goto(position)
        self.original_shape = "artwork/paddle.gif"
        self.long_shape = "artwork/paddle_long.gif"
        self.short_shape = "artwork/paddle_short.gif"
        self.width = 100  # Default width for collision purposes

    def go_left(self):
        new_x = self.xcor() - 20
        if new_x > -280:
            self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        if new_x < 280:
            self.goto(new_x, self.ycor())

    def set_width(self, width):
        self.width = width

    def expand(self):
        self.shape(self.long_shape)
        self.width = 125

    def shrink(self):
        self.shape(self.short_shape)
        self.width = 75

    def revert_size(self):
        self.shape(self.original_shape)
        self.width = 100
