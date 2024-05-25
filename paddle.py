from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("paddle.gif")
        self.penup()
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 20
        if new_x > -280:
            self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        if new_x < 280:
            self.goto(new_x, self.ycor())
