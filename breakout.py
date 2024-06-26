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

        self._register_shapes()
        self.paddle = Paddle((0, -300))
        self.brick_manager = BrickManager()
        self.scoreboard = Scoreboard()
        self.paused = False
        self.game_over = False  # Initialize game_over flag
        self.game_started = False  # Flag to check if the game has started
        self.balls = []  # List to keep track of all balls
        self.timer_id = None

        self._setup_controls()
        self.show_start_screen()
        self.start_level()
        self.add_new_ball()
        self.start_game_loop()
        self.screen.exitonclick()

    def _register_shapes(self):
        """Register custom shapes for game elements"""
        self.screen.register_shape("artwork/paddle.gif")
        self.screen.register_shape("artwork/ball.gif")
        self.screen.register_shape("artwork/brick_red.gif")
        self.screen.register_shape("artwork/brick_orange.gif")
        self.screen.register_shape("artwork/brick_yellow.gif")
        self.screen.register_shape("artwork/brick_green.gif")
        self.screen.register_shape("artwork/brick_blue.gif")
        self.screen.register_shape("artwork/brick_grey.gif")
        self.screen.register_shape("artwork/extra_life.gif")
        self.screen.register_shape("artwork/increase_speed.gif")
        self.screen.register_shape("artwork/decrease_speed.gif")
        self.screen.register_shape("artwork/expand_paddle.gif")
        self.screen.register_shape("artwork/shrink_paddle.gif")
        self.screen.register_shape("artwork/multi_ball.gif")
        self.screen.register_shape("artwork/paddle_long.gif")
        self.screen.register_shape("artwork/paddle_short.gif")

    def _setup_controls(self):
        """Setup key bindings for game controls"""
        self.screen.listen()
        self.screen.onkeypress(self.paddle.go_left, "Left")
        self.screen.onkeypress(self.paddle.go_right, "Right")
        self.screen.onkey(self.toggle_pause, "space")
        self.screen.onkey(self.start_game, "Return")
        self.screen.onkey(self.restart_game, "r")

        self.screen.onkey(self.next_level, "n")  # Cheat key to go to the next level
        self.screen.onkey(self.reset_ball, "b")  # Cheat key to reset the ball

    def show_start_screen(self):
        self.scoreboard.show_start_screen()

    def start_game(self):
        if not self.game_started:
            self.scoreboard.clear_start_screen()
            self.game_started = True
            self.start_level()
            self.start_game_loop()

    def next_level(self):
        self.scoreboard.increase_level()
        for ball in self.balls:
            ball.increase_speed()
        self.start_level()
        self.reset_all_balls()

    def reset_ball(self):
        self.reset_all_balls()

    def toggle_pause(self):
        if self.game_started and not self.game_over:
            self.paused = not self.paused
            if self.paused:
                self.scoreboard.show_paused()
            else:
                self.scoreboard.clear_paused()
                self.start_game_loop()

    def start_level(self):
        self.brick_manager.create_bricks(self.scoreboard.level)

    def start_game_loop(self):
        if self.timer_id is None:
            self.timer_id = self.screen.ontimer(self.game_loop, 20)

    def game_loop(self):
        if not self.game_over:
            if self.game_started and not self.paused:
                for ball in self.balls:
                    ball.move()
                    self._check_collisions(ball)
                    self._check_misses(ball)
                self._check_level_complete()
                self._move_powerups()
                self._check_powerup_collisions()
                self.screen.update()
                self.timer_id = self.screen.ontimer(self.game_loop, 20)

    def stop_game_loop(self):
        if self.timer_id is not None:
            self.screen.ontimer(None, self.timer_id)  # Cancel the existing timer
            self.timer_id = None

    def clear_all_balls(self):
        """Hide and clear all existing balls"""
        for ball in self.balls:
            ball.hideturtle()
        self.balls.clear()

    def add_new_ball(self):
        """Create and add a new ball to the balls list"""
        ball = Ball()
        ball.reset_speed()
        self.balls.append(ball)

    def reset_all_balls(self):
        """Reset the position and speed of all balls"""
        self.clear_all_balls()
        self.add_new_ball()

    def _check_collisions(self, ball):
        """Check and handle collisions between game elements"""
        self._check_wall_collisions(ball)
        self._check_paddle_collision(ball)
        self._check_brick_collisions(ball)

    def _check_wall_collisions(self, ball):
        """Check and handle collisions with the walls"""
        if ball.xcor() > 285 or ball.xcor() < -285:
            ball.bounce_x()
        if ball.ycor() > 290:
            ball.bounce_y()

    def _check_paddle_collision(self, ball):
        """Check and handle collision with the paddle"""
        if ((self.paddle.ycor() - 10 < ball.ycor() < self.paddle.ycor() + 10) and
                (self.paddle.xcor() - ((self.paddle.width / 2) + 5) < ball.xcor() <
                 self.paddle.xcor() + ((self.paddle.width / 2) + 5))):
            ball.sety(self.paddle.ycor() + 10)  # Adjust ball's position to avoid multiple collision detections
            ball.paddle_bounce(self.paddle)

    def _check_brick_collisions(self, ball):
        """Check and handle collisions with bricks"""
        for brick in self.brick_manager.bricks:
            if ball.distance(brick) < 25:
                if brick.hit():
                    self.brick_manager.remove_brick(brick)
                    self.scoreboard.increase_score()
                ball.bounce_y()
                break

    def _check_misses(self, ball):
        """Check if the ball misses the paddle"""
        if ball.ycor() < -290:
            self.balls.remove(ball)
            ball.hideturtle()
            if not self.balls:  # Check if there are no balls left
                self.scoreboard.decrease_life()
                if self.scoreboard.lives == 0:
                    self.scoreboard.game_over()
                    self.game_over = True
                else:
                    self.reset_all_balls()

    def _check_level_complete(self):
        """Check if all bricks are cleared and level is complete"""
        if not self.brick_manager.bricks:
            self.scoreboard.increase_level()
            for ball in self.balls:
                ball.increase_speed()
            self.start_level()
            self.reset_all_balls()

    def _move_powerups(self):
        for powerup in self.brick_manager.active_powerups:
            powerup.move()
            if powerup.ycor() < -320:
                self.brick_manager.active_powerups.remove(powerup)
                powerup.hideturtle()
                print("Power-up missed and removed")

    def _check_powerup_collisions(self):
        for powerup in self.brick_manager.active_powerups:
            if self.paddle.distance(powerup) < 50:
                print(f"Power-up collected: {powerup.powerup_type}")
                powerup.apply_effect(self)
                self.brick_manager.active_powerups.remove(powerup)
                powerup.hideturtle()

    def restart_game(self):
        self.stop_game_loop()
        self.scoreboard.reset_scoreboard()
        self.paddle.goto(0, -300)
        self.clear_all_balls()
        self.add_new_ball()
        self.start_level()
        self.game_over = False
        self.paused = False
        self.game_started = False
        self.show_start_screen()
        self.start_game_loop()


if __name__ == "__main__":
    BreakoutGame()
