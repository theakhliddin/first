import turtle
# Declare a global variable
angle = 45

turtle.pensize(4)
turtle.pencolor("red")
turtle.fillcolor("blue")


turtle.bgcolor("pink")

def draw_square(size):
    # Use the global variable
    turtle.left(angle)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

def main():
    draw_square(50)
    draw_square(100)
    draw_square(150)
    input("Press any key to continue...")
main()