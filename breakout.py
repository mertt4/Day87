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
        self.paused = False
        self.game_over = False  # Initialize game_over flag

        self.screen.listen()
        self.screen.onkeypress(self.paddle.go_left, "Left")
        self.screen.onkeypress(self.paddle.go_right, "Right")
        self.screen.onkey(self.toggle_pause, "space")
        self.screen.onkey(self.restart_game, "Return")

        self.screen.onkey(self.next_level, "n")  # Cheat key to go to the next level
        self.screen.onkey(self.reset_ball, "r")  # Cheat key to reset the ball

        self.start_level()
        self.game_loop()
        self.screen.exitonclick()

    def next_level(self):
        self.scoreboard.increase_level()
        self.ball.increase_speed()
        self.start_level()
        self.ball.reset_position()

    def reset_ball(self):
        self.ball.reset_position()

    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.scoreboard.show_paused()
        else:
            self.scoreboard.clear_paused()

    def start_level(self):
        self.brick_manager.create_bricks(self.scoreboard.level)

    def restart_game(self):
        self.scoreboard.reset()
        self.paddle.goto(0, -300)
        self.ball.reset_position()
        self.start_level()
        self.game_over = False
        self.paused = False
        self.game_loop()

    def game_loop(self):
        if not self.game_over:
            if not self.paused:
                self.ball.move()

                # Detect collision with walls
                if self.ball.xcor() > 290 or self.ball.xcor() < -290:
                    self.ball.bounce_x()
                if self.ball.ycor() > 290:
                    self.ball.bounce_y()

                # Detect collision with paddle
                if ((self.paddle.ycor() - 10 < self.ball.ycor() < self.paddle.ycor() + 10) and
                        (self.paddle.xcor() - 55 < self.ball.xcor() < self.paddle.xcor() + 55)):
                    self.ball.sety(self.paddle.ycor() + 10)  # Adjust ball's position to avoid multiple collision detections
                    self.ball.paddle_bounce(self.paddle)

                # Detect collision with bricks
                for brick in self.brick_manager.bricks:
                    if self.ball.distance(brick) < 25:
                        if brick.hit():
                            print(f"Brick collision detected: Ball at ({self.ball.xcor()}, {self.ball.ycor()}), Brick at ({brick.xcor()}, {brick.ycor()})")
                            self.brick_manager.bricks.remove(brick)
                            self.scoreboard.increase_score()
                        self.ball.bounce_y()

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
                    self.ball.increase_speed()  # Increase ball speed when leveling up
                    self.start_level()
                    self.ball.reset_position()

            self.screen.update()
            self.screen.ontimer(self.game_loop, 20)


if __name__ == "__main__":
    BreakoutGame()
