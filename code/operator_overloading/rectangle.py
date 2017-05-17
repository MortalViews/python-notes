from math import sqrt
class Point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    def __str__(self):
        return "<POINT: x=%d, y=%d>"%(self.x,self.y)
                

            
 
#     def __repr__(self):
#         return self.__str__()
    
class Segment:
    def __init__(self,start,end):
        self.start = start 
        self.end = end 
    def __len__(self):
        return int(sqrt((self.end.x - self.start.x)**2\
                        +(self.end.y - self.start.y)**2))
        
    def mid(self):
        xm = (self.end.x+self.start.x)/2
        ym = (self.end.y+self.start.y)/2
        return Point(xm,ym)
    
    def __str__(self):
        return "<Segment: (%s)-->(%s)>"%(self.start,self.end)
#     def __repr__(self):
#         return self.__str__()
    
class Rectangle:
    def __init__(self,*points):
#         TODO: sort the check
        if len(points) != 4:
            raise Exception("Rectangle should have four points.")
        self.points = points
        self.sides = self._caculate_sides()
        
    def _caculate_sides(self):
        s1 = Segment(*self.points[:2])
        print(type(s1))
        print(s1)
        s2 = Segment(*self.points[1:3])
        s3 = Segment(*self.points[2:4])
        s4 = Segment(*self.points[::-3])
        return s1,s2,s3,s4
    def area(self):
        return len(self.sides[0])*len(self.sides[1])
    

    def __str__(self):
        return "sides ({}),{},{},{}".format(*self.sides)

a = Point(1,2)
b = Point(1,5)
c = Point(10,5)
d = Point(10,2)
points= (a,b,c,d)
print(points)
if __name__ == '__main__':
    r = Rectangle(a,b,c,d)
    print(str(r))
    print(r.area())
        