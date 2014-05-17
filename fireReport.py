import turtle
import math
NUMBER_OF_LICENSES=10

def goodbyeMessage():
    print("Thank you for using the program!")

def getInfo():
    fire_Direction=math.radians(float(input("Please input the angle in degrees of the fire quickly!")))
    fire_Distance=float(input("Please input the distance of the fire ~VERY~ quickly (input a number between 1 and 5)"))
    return fire_Direction,fire_Distance


def announceDirections(horizontolDirection,verticalDirection):

    sideOfFireHouseToLeaveFrom=[]
    
    if horizontolDirection < 0:
        print("The fire is %d streets to the west of the firehouse!" %horizontolDirection)
        sideOfFireHouseToLeaveFrom.append('west')
    elif horizontolDirection > 0:
        print("The fire is %d streets to the east of the firehouse!" %horizontolDirection)
        sideOfFireHouseToLeaveFrom.append("east")
    else:
        sideOfFireHouseToLeaveFrom.append("void")
    
    if verticalDirection < 0:
        print("The fire is %d streets to the south of the firehouse!" %verticalDirection)
        sideOfFireHouseToLeaveFrom.append("south")
    elif verticalDirection > 0:
        print("The fire is %d streets to the north of the firehouse!" %verticalDirection)
        sideOfFireHouseToLeaveFrom.append("north")
    else:
        pass

    if verticalDirection == 0 and horizontolDirection == 0:
        print("The firehouse is on fire!")
        sideOfFireHouseToLeaveFrom.append("void")
        sideOfFireHouseToLeaveFrom.append("void")
        

    return sideOfFireHouseToLeaveFrom
    
def gotoFire(horizontolDirection,verticalDirection,sideOfFireHouseToLeaveFrom):

    
    
    if sideOfFireHouseToLeaveFrom[0] == "east":
        turtle.forward(300)
        turtle.right(90)
        

    elif sideOfFireHouseToLeaveFrom[0] == "west":
        turtle.forward(200)
        turtle.right(90)
        
    else:
        pass

    if sideOfFireHouseToLeaveFrom[1] == "north":
        turtle.forward(200)
        
    elif sideOfFireHouseToLeaveFrom[1] == "south":
        turtle.forward(300)
        
    else:
        pass

    turtle.pendown()
    turtle.color("blue")
    if sideOfFireHouseToLeaveFrom[1] == "north":
        turtle.right(180)
        turtle.forward((verticalDirection * 100)-100)
        turtle.right(180)
    elif sideOfFireHouseToLeaveFrom[1] == "south":
        turtle.forward(verticalDirection * 100)

    if sideOfFireHouseToLeaveFrom[0] == "west":
        turtle.left(90)
        turtle.forward(horizontolDirection * 100)
        
    elif sideOfFireHouseToLeaveFrom[0] == "east":
        turtle.right(90)
        turtle.forward(horizontolDirection * 100)
    
    turtle.done()        
        

    

        

    


def giveDirection(fire_Direction,fire_Distance):
    horizontolDirection = int(abs(round(fire_Distance * (math.cos(fire_Direction)))))
    verticalDirection = int(abs(round(fire_Distance * (math.sin(fire_Direction)))))
    sideOfFireHouseToLeaveFrom = announceDirections(horizontolDirection,verticalDirection)

    gotoFire(horizontolDirection,verticalDirection,sideOfFireHouseToLeaveFrom)


    
    return horizontolDirection, verticalDirection
    
    

def reportFire():
    
    fire_Direction,fire_Distance=getInfo()
    horizontolDirection,verticalDirection = giveDirection(fire_Direction,fire_Distance)



def drawHorizontal():
    turtle.speed(0)
    turtle.penup()
    turtle.forward(-300)
    turtle.left(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.pendown()
    for i in range(5):
        turtle.forward(500)
        turtle.forward(-500)
        turtle.right(90)
        turtle.forward(100)
        turtle.left(90)

    turtle.forward(500)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(180)

def drawVertical():
    for i in range(5):
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(500)
            turtle.forward(-500)
            turtle.left(90)
    turtle.forward(-500) #Back to upper left corner which will be main drawing control point

def drawFireStation():
    #From main drawing control point
    turtle.penup()
    #225 instead of 250 so firestation circle is centered in middle of grid
    turtle.forward(225)
    turtle.right(90)
    turtle.forward(250)
    turtle.pendown()
    turtle.circle(25)
    turtle.penup()
    turtle.forward(-250)
    turtle.left(90)
    turtle.forward(-225)
def drawGrid():
    turtle.showturtle()
    turtle.speed(0)
    drawHorizontal()
    drawVertical()
    drawFireStation()
    
    

def main():
    drawGrid()
    for i in range(NUMBER_OF_LICENSES):
        reportFire()
    goodbyeMessage()

if __name__ == "__main__":
    main()
