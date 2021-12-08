import time
from cars import Cars
from player import Player
from scoreboard import Scoreboard
from turtle import Screen

screen = Screen()
screen.title("Turtle crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
screen.onkeypress(fun=player.move, key="Up")
cars = Cars()
game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()

    for car in cars.cars:
        car.move()

    for car in cars.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_on = False
            break

    if player.ycor() > 280:
        player.level_up()
        scoreboard.increase_level()
        for car in cars.cars:
            car.increase_speed()

screen.exitonclick()
