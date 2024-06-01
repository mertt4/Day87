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
        self.max_speed = 0.9  # Maximum move speed
        self.move_speed = self.initial_speed
        self.x_move = 5
        self.y_move = 5

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
        new_speed = self.move_speed * 0.9  # Reduce delay (increase speed)
        self.move_speed = max(new_speed, self.min_speed)  # Cap at min_speed
        print(f"Increased speed, new move_speed: {self.move_speed}")

    def decrease_speed(self):
        new_speed = self.move_speed / 0.9  # Increase delay (decrease speed)
        self.move_speed = min(new_speed, self.max_speed)  # Cap at max_speed
        print(f"Decreased speed, new move_speed: {self.move_speed}")

    def reset_speed(self):
        self.move_speed = self.initial_speed
        print(f"Reset speed, new move_speed: {self.move_speed}")
