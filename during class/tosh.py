import turtle as t

def drawlines ():
    t.forward(100)
    t.left(87)
    t.setheading(127)
    t.down()
    t.goto(50, 50)
    t.home()
    t.circle(25)

def main():
    drawlines()
    input('press enter to exit')

main()