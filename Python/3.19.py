import turtle


def main():

    pointOneX = int(input("Please enter x coordinate of first point"))
    pointOneY = int(input("Please enter y coordinate of first point"))

    pointTwoX = int(input("Please enter x coordinate of second point"))
    pointTwoY = int(input("Please enter y coordinate of second point"))

    turtle.speed(0)
    turtle.penup()
    turtle.goto(pointOneX,pointOneY)
    turtle.pendown()
    turtle.write((pointOneX,pointOneY))
    turtle.goto(pointTwoX,pointTwoY)
    turtle.write((pointTwoX,pointTwoY))
    turtle.done()


if __name__ == "__main__":
    main()
