from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("artwork/ball.gif")
        # self.color("white")
        self.penup()
        self.speed(0)  # Fastest animation speed
        self.initial_speed = 0.1  # Initial move speed (delay between movements)
        self.min_speed = 0.02  # Minimum move speed (to prevent too fast movement)
        self.move_speed = self.initial_speed
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def paddle_bounce(self, paddle):
        self.y_move *= -1
        # Modify x_move based on where it hit the paddle
        offset = self.xcor() - paddle.xcor()
        self.x_move = offset * 0.2

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_y()

    def increase_speed(self):
        self.move_speed *= 0.9  # Increase speed by 10%

    def decrease_speed(self):
        self.move_speed /= 0.9  # Decrease speed by 10%

    def reset_speed(self):
        self.move_speed = self.initial_speed
