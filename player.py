from turtle import Turtle

SPEED = 10
STARTING_POS = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setpos(STARTING_POS)
        self.setheading(90)

    def move(self):
        self.forward(SPEED)

    def level_up(self):
        self.setpos(STARTING_POS)
