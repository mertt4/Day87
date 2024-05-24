from turtle import Turtle

LIVES = 5


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = LIVES
        self.level = 1
        self.high_score = self.load_high_score()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 275)
        self.write(f"Score: {self.score} Lives: {self.lives} Level: {self.level} High Score: {self.high_score}",
                   align="center", font=("Courier", 14, "normal"))

    def increase_score(self):
        self.score += 10
        self.update_scoreboard()

    def decrease_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 36, "normal"))
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except:
            return 0

    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def show_paused(self):
        self.goto(0, 0)
        self.write("PAUSED", align="center", font=("Courier", 24, "normal"))

    def clear_paused(self):
        self.clear()
        self.update_scoreboard()

    def reset(self):
        self.score = 0
        self.lives = LIVES
        self.level = 1
        self.update_scoreboard()
