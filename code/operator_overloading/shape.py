# TODO: len should give the actual length covered by 
# the path

class Point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 

class Path: 
    
    def __init__(self):
        self.points = []
    
    def add(self,*points):
        self.points.extend(points)
    
    def travel(self):
        pass 
    
    def num_len(self):
        return len(self.points)

    def __len__(self):
        pass 
        

        
    
p1 = Path()
a1 = Point(0,0)
p1.add(a1)
points = [(1,2),(4,5),(5,6)]

# adding 1 point objecdt at a time
[p1.add(Point(*c)) for c in points]

points = [(1,3),(4,5)]

# create a list of point objects
list_of_point_obj = [Point(*i) for i in points]

p1.add(*list_of_point_obj)

print(p1.num_len)


# Two cases:
# 1.) p1.add(point)
# 2.) p1.add([point,point])
