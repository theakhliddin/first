import turtle

def drawlines ():
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.down()
    turtle.goto(50, 50)
    turtle.home()
    turtle.circle(25)

def main():
    drawlines()
    input('press enter to exit')

main()