from turtle import Turtle


class Brick(Turtle):
    def __init__(self, position, hits=1, color="blue"):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.penup()
        self.color(color)
        self.goto(position)
        self.hits = hits
        self.initial_color = color

    def hit(self):
        self.hits -= 1
        if self.hits > 0:
            self.color("gray")  # Change color to indicate damage
            return False  # Brick is not yet destroyed
        else:
            self.hideturtle()
            return True  # Brick is destroyed
