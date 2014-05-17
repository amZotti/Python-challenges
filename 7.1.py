class Rectangle:
    def __init__(self, width = 1.0, height = 2.0):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return (self.width * 2) + (self.height * 2)

        
def main():

    r1 = Rectangle(4, 40)
    r2 = Rectangle(3.5, 35.7)

    print("Rectangle 1: \n\
    Width: %f\n\
    Height: %f\n\
    Area: %f\n\
    Perimeter: %f\n\n" % (r1.width, r1.height, r1.getArea(), r1.getPerimeter()))

    print("Rectangle 2:\n \
    Width: %f\n\
    Height: %f\n\
    Area: %f\n\
    Perimeter: %f\n" % (r2.width, r2.height, r2.getArea(), r2.getPerimeter()))

if __name__ == "__main__":
    main()
