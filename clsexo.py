class Point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    def __repr__(self):
        return "(%s,%s)"%(self.x,self.y)
        
class Path:
    def __init__(self):
        self.points = []
    
    def connect(self,point):
        self.points.append(point)
        return self 
    
    def __repr__(self):
        s = ''
        for i in self.points:
            s+="(%s,%s)-->"%(i.x,i.y)
        return s.rstrip('-->')
    
        
p1 = Point(4,6)
p2 = Point(7,7)
p3 = Point(7,10)

path1 = Path()
path2 = Path()

# path1.connect(p1).connect(p2)
path1.connect(p1)\
        .connect(p2)\
        .connect(p3)
# "(2,4)-->(2,4)-->(1,3)
print(path1)
