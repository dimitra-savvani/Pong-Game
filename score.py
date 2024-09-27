from turtle import Turtle
SCOREBOARD_X_POS = 50
SCOREBOARD_Y_POS = 240

class ScoreBoard(Turtle):
    def __init__(self, side):
        super().__init__()
        self.score = 0
        self.side = side
        self.create()

    def create(self):
        self.penup()
        self.hideturtle()
        self.color('white')
        if self.side == "right":
            self.goto(SCOREBOARD_X_POS, SCOREBOARD_Y_POS)
        else:
            self.goto(-SCOREBOARD_X_POS, SCOREBOARD_Y_POS)
        self.write(f"{self.score}", align='center', font=('Arial', 36, 'bold'))

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align='center', font=('Arial', 36, 'bold'))





