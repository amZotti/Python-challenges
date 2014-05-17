import sys

class fan:
    def __init__(self,radius = 5,speed = 1,color = 'blue',on = False):

        self.radius = radius
        self.on = on
        self.speed = speed
        self.color = color
        
    def getSpeed(self):
        return self.speed

    def setSpeed(self,speed):
        self.speed = speed

    def getRadius(self):
        return self.radius

    def setRadius(self,radius):
        self.radius = radius

    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color = color

    def getOn(self):
        return on

    def setOn(self, on):
        self.on = on
        


        
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv[0]))
print("The arguments are: ", str(sys.argv[0]))
for argument in range(5):
    print(sys.argv[argument])

