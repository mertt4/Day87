from turtle import Turtle


class BrickManager:
    def __init__(self):
        self.bricks = []
        self.create_bricks()

    def create_bricks(self):
        colors = ['red', 'orange', 'yellow', 'green', 'blue']
        y_positions = [250, 220, 190, 160, 130]
        for color, y in zip(colors, y_positions):
            for x in range(-275, 300, 50):
                brick = Turtle("square")
                brick.color(color)
                brick.shapesize(stretch_wid=1, stretch_len=2)
                brick.penup()
                brick.goto(x, y)
                self.bricks.append(brick)
