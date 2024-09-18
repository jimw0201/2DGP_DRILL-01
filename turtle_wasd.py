import turtle

def move_up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def move_left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def move_right():
    turtle.setheading(360)
    turtle.forward(50)
    turtle.stamp()

def move_down():
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.stamp()

turtle.shape('turtle')

turtle.stamp()

turtle.onkey(move_up, 'w')
turtle.listen()

turtle.onkey(move_left, 'a')
turtle.listen()

turtle.onkey(move_right, 'd')
turtle.listen()

turtle.onkey(move_down, 's')
turtle.listen()
