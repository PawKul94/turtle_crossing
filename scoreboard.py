from turtle import Turtle

FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 0
        self.penup()
        self.setpos(-280, 260)
        self.write_score()

    def write_score(self):
        self.clear()
        self.pendown()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.write_score()

    def game_over(self):
        self.home()
        self.write("Game over.", align="center", font=FONT)
