import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "brown", "black"]
STARTING_SPEED = 5


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.speed = STARTING_SPEED
        self.penup()
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.setpos(random.randrange(310, 1010, 40), random.randrange(-240, 260, 30))
        self.shapesize(stretch_wid=1, stretch_len=2)

    def move(self):
        self.forward(self.speed)
        self.reset_position()

    def reset_position(self):
        if self.xcor() < -310:
            self.setpos(310, random.randrange(-240, 260, 20))

    def increase_speed(self):
        self.speed += 2


class Cars:
    def __init__(self):
        self.cars = [Car() for _ in range(40)]
