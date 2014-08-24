import turtle

turtle.speed(0)
turtle.penup()
def mousefunction(x,y):
    turtle.goto(x,y)
    turtle.write("%+.1f %+.1f" % (x,y), x,y)

turtle.onscreenclick(mousefunction)

done()
