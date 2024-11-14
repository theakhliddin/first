import turtle as t

t.speed(8)

def pixel():
    i=0
    while  i<4:
        t.forward(30)
        t.left(90)
        i=i+1
   
def row():
    i=0
    while i<20:
        pixel()
        t.forward(30)
        i=i+1

def sev():
    i=0
    while i<5:
        t.down()
        row()
        xpos = t.xcor(-300)
        ypos = t.ycor(250)
        t.up()
        t.goto(-int(xpos), int(ypos-30))
        i=i+1

def main():
    t.penup()
    t.goto(-300, 250)
    t.pendown()
    pixel()
    row()
    sev()
    t.done()
    
if  __name__ == "__main__":
    main()
