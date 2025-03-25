import turtle as t
t.speed(0)
t.tracer(True)
t.bgcolor("green")
t.pencolor("orange")

def centered_cirlce(x, y, r, color, angle = 360):
    t.setheading(0)
    t.penup()
    t.goto(x, y)
    t.forward(r)
    t.left(90)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r, angle)
    t.end_fill()
    t.penup()

def draw_nose(x, y, r, face_color):
    centered_cirlce(x, y, r, face_color)
    centered_cirlce(x, y, r/10, "pink")

def draw_eye(x, y, r, color):
    centered_cirlce(x, y, r, "white")
    centered_cirlce(x, y, (r*2)/3 , color)
    centered_cirlce(x, y, r/3, "black")

def smiley(x, y, r, eye_color):
    draw_nose(x, y, r, "yellow")
    draw_eye(x + r*6/20 , y + r*5/20, r*5/20, eye_color)
    draw_eye(x - r*6/20 , y + r*5/20, r*5/20, eye_color)
    centered_cirlce(x, y - r*4/20 , r *6/20, "red", -180)

smiley(20, 20, 70, "brown")
smiley(0, 200, 50, "green")
smiley(200, 30, 50, "blue")

input("Press Enter to continue...")