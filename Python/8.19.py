def main():
    

    r1 = Rectangle2D(*[float(i) for i in input('Enter x1, y1, width1, height1: ').split(',')])
    r2 = Rectangle2D(*[float(i) for i in input('Enter x2, y2, width2, height2: ').split(',')])    

    print("Area for r1 is",r1.getArea())
    print("Perimeter for r1 is",r1.getPerimeter())
    print("Area for r2 is",r2.getArea())
    print("Perimeter for r2 is",r2.getPerimeter())
    print("r1 contains the center of r2?",r1.containsPoint(r2.getX()\
                                                           ,r2.getY()))
    print("r1 contains r2?",r1.contains(r2))
    print("r1 overlaps r2?",r1.overlaps(r2))




class Rectangle2D:

    def __init__(self, x = 0.0, y = 0.0, width = 0.0, height = 0.0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        #Boundaries of Rectangle
        self.left_boundary = self.x - (self.width/2)
        self.right_boundary = self.x + (self.width/2)
        self.up_boundary = self.y + (self.height/2)
        self.down_boundary = self.y - (self.height/2)

        #Intervals
        self.x_interval = [self.left_boundary,self.right_boundary]
        self.y_interval = [self.down_boundary,self.up_boundary]

    def getX(self):
        return self.x

    def setX(self,x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self,y):
        self.y = y

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

    def getWidth(self):
        return self.width

    def setWidth(self, width):
        self.width = width

    def getArea(self):
        return (self.width * self.height)

    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def containsPoint(self,point_x,point_y):
        y_aligned = False
        x_aligned = False
        
        #Aligned on x axis?
        if point_x >= self.left_boundary and \
           point_x <= self.right_boundary:
            x_aligned = True

        #Aligned on y axis?
        if point_y <= self.up_boundary and\
           point_y >= self.down_boundary:
            y_aligned = True

        if y_aligned and x_aligned:
            return True
        else:
            return False

    def contains(self,Rectangle2D):
        x1 = self.x_interval
        x2 = Rectangle2D.x_interval
        y1 = self.y_interval
        y2 = Rectangle2D.y_interval
        x_interception = False
        y_interception = False
        
        #Is either end within the other rectangle?
        if (x2[0] > x1[0] and x2[0] < x1[1]) or (x2[1] > x1[0] and x2[1] < x1[1]):
            x_interception = True
        else:
            x_interception = False
            
        if (y2[0] > y1[0] and y2[0] < y1[1]) or (y2[1] > y1[0] and y2[1] < y1[1]):
            y_interception = True
        else:
            y_interception = False

        if x_interception and y_interception:
            return True
        else:
            return False

    def overlaps(self,Rectangle2D):   
        if (self.left_boundary < Rectangle2D.right_boundary \
            and self.right_boundary > Rectangle2D.left_boundary\
            and self.down_boundary < Rectangle2D.up_boundary\
            and self.up_boundary > Rectangle2D.down_boundary):
            return True
        else:
            return False

    def __contains__(self,another):
        return self.contains(another)

    def __cmp__(self, other):
        if self.getArea() < other.getArea() : return -1
        elif self.getArea() == other.getArea() : return 0
        elif self.getArea() > other.getArea() : return 1

    def __lt__(self, other):
        return self.getArea() < other.getArea()

    def __le__(self, other):
        return self.getArea() <= other.getArea()
        

    def __eq__(self, other):
        return self.getArea() == other.getArea()

    def __ne__(self, other):
        return self.getArea() != other.getArea()

    def __gt__(self, other):
        return self.getArea() > other.getArea()

    def __ge__(self, other):
        return self.getArea() >= other.getArea()

    
        


if __name__ == "__main__":
    main()

        
