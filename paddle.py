from turtle import Turtle
PADDLE_TILES = 5
PADDLE_X_POS = 350
HEIGHT_LIMIT = 250
PADDLE_STEP = 20


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.create()

    def create(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.penup()
        self.speed("fastest")

        if self.side == 'left':
            x_pos = -PADDLE_X_POS
        else:
            x_pos = PADDLE_X_POS

        self.goto(x_pos, 0)

    def up(self):
        #move upwards
        if self.ycor() < HEIGHT_LIMIT:
            self.fd(PADDLE_STEP)


    def down(self):
        # move downwards
        if self.ycor() > -HEIGHT_LIMIT:
            self.bk(PADDLE_STEP)