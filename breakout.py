from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick_manager import BrickManager
from scoreboard import Scoreboard


class BreakoutGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=650)
        self.screen.bgcolor("black")
        self.screen.title("Breakout")
        self.screen.tracer(0)

        self.paddle = Paddle((0, -300))
        self.ball = Ball()
        self.brick_manager = BrickManager()
        self.scoreboard = Scoreboard()

        self.game_over = False  # Initialize game_over flag

        self.screen.listen()
        self.screen.onkeypress(self.paddle.go_left, "Left")
        self.screen.onkeypress(self.paddle.go_right, "Right")

        self.start_level()
        self.game_loop()
        self.screen.exitonclick()

    def start_level(self):
        self.brick_manager.create_bricks(self.scoreboard.level)

    def game_loop(self):
        if not self.game_over:
            self.ball.move()

            # Detect collision with walls
            if self.ball.xcor() > 290 or self.ball.xcor() < -290:
                self.ball.bounce_x()
            if self.ball.ycor() > 290:
                self.ball.bounce_y()

            # Detect collision with paddle
            if ((self.paddle.ycor() - 10 < self.ball.ycor() < self.paddle.ycor() + 10) and
                    (self.paddle.xcor() - 55 < self.ball.xcor() < self.paddle.xcor() + 55)):
                print(
                    f"Paddle collision detected: Ball at ({self.ball.xcor()}, {self.ball.ycor()}), Paddle at "
                    f"({self.paddle.xcor()}, {self.paddle.ycor()})")
                self.ball.sety(self.paddle.ycor() + 10)  # Adjust ball's position to avoid multiple collision detections
                self.ball.bounce_y()

            # Detect collision with bricks
            for brick in self.brick_manager.bricks:
                if self.ball.distance(brick) < 25:
                    print(f"Brick collision detected: Ball at ({self.ball.xcor()}, {self.ball.ycor()}), Brick at ({brick.xcor()}, {brick.ycor()})")
                    self.brick_manager.bricks.remove(brick)
                    brick.hideturtle()
                    self.ball.bounce_y()
                    self.scoreboard.increase_score()

            # Detect if ball misses paddle
            if self.ball.ycor() < -290:
                print("Ball missed paddle")
                self.scoreboard.decrease_life()
                if self.scoreboard.lives == 0:
                    print("Game Over")
                    self.scoreboard.game_over()
                    self.game_over = True
                else:
                    self.ball.reset_position()

            # Check if all bricks are cleared
            if not self.brick_manager.bricks:
                self.scoreboard.increase_level()
                self.start_level()
                self.ball.reset_position()

            self.screen.update()
            self.screen.ontimer(self.game_loop, 20)


if __name__ == "__main__":
    BreakoutGame()