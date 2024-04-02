from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Keeps score"""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(x=-220, y=260)
        self.scoreboard()

    def scoreboard(self):
        self.write(f"Level: {self.level}", align= "center", font=FONT)

    def keep_level(self):
        self.level += 1

    def game_over(self):
        game_over = Turtle()
        game_over.penup()
        game_over.write("GAME OVER", align="center", font=FONT)
