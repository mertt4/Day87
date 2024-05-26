from turtle import Turtle
import random


class PowerUp(Turtle):
    def __init__(self, powerup_type, position):
        super().__init__()
        self.powerup_type = powerup_type
        self.shape("circle")
        self.color('white')
        self.penup()
        self.goto(position)
        self.setheading(-90)  # Fall downwards
        print(f"PowerUp created: {self.powerup_type} at {self.position()}")

    def move(self):
        self.forward(10)

    def apply_effect(self, game):
        if self.powerup_type == "expand_paddle":
            pass
        elif self.powerup_type == "shrink_paddle":
            pass
        elif self.powerup_type == "extra_life":
            game.scoreboard.lives += 1
            game.scoreboard.update_scoreboard()
        elif self.powerup_type == "increase_speed":
            game.ball.increase_speed()
        elif self.powerup_type == "decrease_speed":
            game.ball.decrease_speed()
        elif self.powerup_type == "multi_ball":
            # game.add_ball()
            pass
