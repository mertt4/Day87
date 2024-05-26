import random
from turtle import Turtle
from ball import Ball


class PowerUp(Turtle):
    def __init__(self, powerup_type, position):
        super().__init__()
        self.powerup_type = powerup_type
        self.powerup_shape()
        self.penup()
        self.goto(position)
        self.setheading(-90)  # Fall downwards
        print(f"PowerUp created: {self.powerup_type} at {self.position()}")

    def powerup_shape(self):
        if self.powerup_type == "expand_paddle":
            self.shape("artwork/expand_paddle.gif")
        elif self.powerup_type == "shrink_paddle":
            self.shape("artwork/shrink_paddle.gif")
        elif self.powerup_type == "extra_life":
            self.shape("artwork/extra_life.gif")
        elif self.powerup_type == "increase_speed":
            self.shape("artwork/increase_speed.gif")
        elif self.powerup_type == "decrease_speed":
            self.shape("artwork/decrease_speed.gif")
        elif self.powerup_type == "multi_ball":
            self.shape("artwork/multi_ball.gif")

    def move(self):
        self.forward(10)

    def apply_effect(self, game):
        if self.powerup_type == "expand_paddle":
            self.expand_paddle(game.paddle, game.screen)
        elif self.powerup_type == "shrink_paddle":
            self.shrink_paddle(game.paddle, game.screen)
        elif self.powerup_type == "extra_life":
            game.scoreboard.lives += 1
            game.scoreboard.update_scoreboard()
        elif self.powerup_type == "increase_speed":
            game.ball.increase_speed()
        elif self.powerup_type == "decrease_speed":
            game.ball.decrease_speed()
        elif self.powerup_type == "multi_ball":
            self.multi_ball(game)

    def expand_paddle(self, paddle, screen):
        paddle.expand()
        screen.ontimer(lambda: paddle.revert_size(), 10000)
        self.hideturtle()

    def shrink_paddle(self, paddle, screen):
        paddle.shrink()
        screen.ontimer(lambda: paddle.revert_size(), 10000)
        self.hideturtle()

    def multi_ball(self, game):
        # Create additional balls and add them to the game
        for _ in range(2):  # add two more balls
            new_ball = Ball()
            new_ball.goto(game.ball.position())
            new_ball.setheading(random.randint(0, 360))  # set a random direction for the new ball
            game.balls.append(new_ball)
        self.hideturtle()
