class shape:
    def area(self):
        print("calculating area....")

class circle(shape):
    def __init__(self,radious):
        self.radious=radious

    def area(self):
        return 3.14*(self.radious ** 2)
    
class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth
    
s=shape()
c=circle(6)
s.area()
print(c.area())
r=rectangle(5,4)
print(r.area())

