from turtle import Turtle
UPWARDS = 1
DOWNWARDS = -1
RIGHT = 1
LEFT = -1
BALL_STEP = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.speed('fastest')
        self.move_speed = 0.1
        self.x_direction = RIGHT
        self.y_direction = UPWARDS

    def move(self):
        if self.wall_collision():
            self.reverse_direction("y")
        self.goto(self.xcor() + self.x_direction*BALL_STEP, self.ycor() + self.y_direction*BALL_STEP)

    def wall_collision(self):
        return abs(self.ycor()) > 280

    def reverse_direction(self, axis):
        if axis == 'x':
            self.x_direction *= -1
        if axis == 'y':
            self.y_direction *= -1

    def hit_paddle(self, r_paddle, l_paddle):
        if self.distance(r_paddle) < 50 or self.distance(l_paddle) < 50:
            self.reverse_direction("x")
            self.move_speed *= 0.9
            return True
        else:
            return False

    def reset(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.reverse_direction("x")

