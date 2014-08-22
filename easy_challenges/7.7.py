class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def getb(self):
        return self.b

    def geta(self):
        return self.a

    def getc(self):
        return self.c

    def getd(self):
        return self.d

    def gete(self):
        return self.e
    
    def getf(self):
        return self.f
    def isSolvable(self):
        if ((self.a * self.d) - (self.b * self.c)) != 0:
            return True
        else:
            return False
    def getX(self):
        x =((self.e * self.d) - (self.b * self.f)) / \
                 ((self.a * self.d) * (self.b * self.c))
        return x
    def getY(self):
        return ((self.a * self.f) - (self.e * self.c))/\
                 ((self.a * self.d) - (self.b * self.c))

equation1 = LinearEquation(2,4,1,4,5,2)
