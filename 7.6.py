import math

class quadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def geta(self):
        return a
    def seta(a):
        self.a = a
    def getb(self):
        return self.b
    def setb(self,b):
        self.b = b
    def getc(self):
        return self.c
    def setc(self, c):
        self.c = c
    def getDiscriminate(self):
        return ((self.b * self.b)-(4*self.a*self.c))
    def getroot1(self):
       return ((-self.b) + math.sqrt( (self.b * self.b) - (4 * self.a * self.c)))/(2*self.a)
    def getroot2(self):
        return ((-self.b) + math.sqrt( (self.b * self.b) - (4 * self.a * self.c)))/(2*self.a)
