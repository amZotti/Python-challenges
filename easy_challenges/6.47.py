import turtle


def square(SIZE):
    turtle.setheading(0)
    turtle.forward(SIZE)
    turtle.right(90)
    turtle.forward(SIZE)
    turtle.right(90)
    turtle.forward(SIZE)
    turtle.right(90)
    turtle.forward(SIZE)
    turtle.right(90)
    turtle.forward(SIZE)

def fillSquare(SIZE):
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(SIZE)
    turtle.right(90)
    turtle.forward(SIZE)
    turtle.right(90)
    turtle.forward(SIZE)
    turtle.right(90)
    turtle.forward(SIZE)
    turtle.right(90)
    turtle.forward(SIZE)
    turtle.end_fill()


def main():
    drawChessboard(-400,400,400,-400)
    drawChessboard(50,-50,400,-400)

def drawChessboard(startx, endx, starty, endy):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(startx,starty)
    turtle.pendown()
    SIZE = 50
    for i in range(4):
        for i in range(4):
            square(SIZE)
            fillSquare(SIZE)
        turtle.setheading(0)
        turtle.forward(-SIZE * 8)
        turtle.setheading(270)
        turtle.forward(SIZE)
        for i in range(4):
            fillSquare(SIZE)
            square(SIZE)
        turtle.setheading(0)
        turtle.forward(-SIZE * 8)
        turtle.setheading(270)
        turtle.forward(SIZE)
        
            
        
        turtle.setheading(270)
   
    
if __name__ == "__main__":
    main()
turtle.done()
