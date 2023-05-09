import turtle

# Set up the game window
win = turtle.Screen()
win.title("Breakout Game")
win.bgcolor("black")
win.setup(width=600, height=800)

# Create the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -350)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Create the bricks
bricks = []
for i in range(-200, 200, 50):
    for j in range(250, 350, 25):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color("red")
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        brick.goto(i, j)
        bricks.append(brick)

# Move the paddle left and right
def move_left():
    x = paddle.xcor()
    if x > -250:
        x -= 20
    paddle.setx(x)

def move_right():
    x = paddle.xcor()
    if x < 250:
        x += 20
    paddle.setx(x)

# Set up the keyboard bindings
win.listen()
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for wall collisions
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1
    if ball.ycor() > 390:
        ball.dy *= -1

    # Check for paddle collision
    if ball.ycor() < -340 and ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50:
        ball.dy *= -1

    # Check for brick collision
    for brick in bricks:
        if ball.distance(brick) < 40:
            brick.goto(1000, 1000) # move brick offscreen
            ball.dy *= -1

