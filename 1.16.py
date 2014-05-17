import turtle

def main():
    #Go to first and fourth circles and draw them
    
    turtle.speed(0)
    turtle.penup()
    turtle.forward(45)
    turtle.pendown()
    turtle.circle(45)
    turtle.circle(-45)
   
    

    #Draw second circle set
    turtle.up()
    turtle.forward(-90)
    turtle.pendown()
    turtle.circle(45)
    turtle.circle(-45)
    turtle.done()



if __name__ == "__main__":
    main()
