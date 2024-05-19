from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  Lives: {self.lives}", align="center", font=("Courier", 24, 'normal'))

    def increase_score(self):
        self.score += 10
        self.update_score()

    def decrease_life(self):
        self.lives -= 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 36, "normal"))
