class Point:
    def __init__(self, x=0,y=0):
        self.x= x
        self.y= y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
point1=Point(1,8)
print(point1)        
point2=Point(20,89)
print(point2)