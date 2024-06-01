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
        self.forward(5)

    def apply_effect(self, game):
        if self.powerup_type == "expand_paddle":
            self.expand_paddle(game.paddle, game.screen)
        elif self.powerup_type == "shrink_paddle":
            self.shrink_paddle(game.paddle, game.screen)
        elif self.powerup_type == "extra_life":
            game.scoreboard.lives += 1
            game.scoreboard.update_scoreboard()
        elif self.powerup_type == "increase_speed":
            game.balls.increase_speed()
        elif self.powerup_type == "decrease_speed":
            game.balls.decrease_speed()
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
        existing_balls = game.balls.copy()
        for ball in existing_balls:
            for _ in range(2):  # Create two new balls for each existing ball
                new_ball = Ball()
                new_ball.goto(ball.xcor(), ball.ycor())
                new_ball.x_move = ball.x_move
                new_ball.y_move = -ball.y_move  # reverse the y for some variation
                new_ball.move_speed = ball.move_speed
                game.balls.append(new_ball)
