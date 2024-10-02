from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from score import ScoreBoard

HIT_PADDLE_LIMIT = 330
DEFINITELY_MISSED = 340

if __name__ == "__main__":

    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    screen.title("Pong")
    screen.tracer(0)

    # creating paddles
    right_paddle = Paddle('right')
    left_paddle = Paddle('left')
    ball = Ball()
    right_score = ScoreBoard('right')
    left_score = ScoreBoard('left')
    screen.update()

    screen.listen()
    screen.onkeypress(right_paddle.up, "Up")
    screen.onkeypress(right_paddle.down, "Down")
    screen.onkeypress(left_paddle.up, "w")
    screen.onkeypress(left_paddle.down, "s")

    game_is_on = True

    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        if abs(ball.xcor()) > HIT_PADDLE_LIMIT:
            ball.hit_paddle(right_paddle, left_paddle)
        if ball.xcor() > DEFINITELY_MISSED:
            left_score.update()
            if left_score.score > 10:
                game_is_on = False
            ball.reset()
        elif ball.xcor() < -DEFINITELY_MISSED:
            right_score.update()
            print(right_score.score)
            if right_score.score > 10:
                game_is_on = False
            ball.reset()

    # Declare winner
    right_score.clear()
    left_score.clear()
    right_score.goto(0, 0)
    score_difference = abs(right_score.score - left_score.score)
    if score_difference == 1:
        string = ""
    else:
        string = "s"
    if right_score.score > left_score.score:
        right_score.write(f"Right player won with {score_difference} point{string} over Left player!!", align='center', font=('Arial', 20, 'bold'))
    else:
        right_score.write(f"Left player won with {score_difference} point{string} over Right player!!", align='center', font=('Arial', 20, 'bold'))


    screen.exitonclick()
