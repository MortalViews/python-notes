s = 'sanjay'
i = 1
a = {'x':1,'y':3}
b = {'x':2,'y':4}

def log(msg):
    print(msg)
    
class Point:

    def __init__(self,x,y):
        self.x = x 
        self.y = y 
        
    def __add__(self,other):
        x = self.x+other.x 
        y = self.y+other.y
        return Point(x,y)
    
    def __sub__(self,other):
        x = self.x - other.x 
        y = self.y - other.y
        return Point(x,y)
        
    def __str__(self):
        return "(x=%s, y=%s)"%(self.x,self.y)


class Rectangle:
    def __init__(self,a,b,c,d):
        self.a = a 
        self.b = b 
        self.c = c 
        self.d = d 
    
    def area(self):
#         TODO
        pass 


class Segment:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def __str__(self):
        return "%s --> %s" %(str(self.a),self.b)
      
    def __len__(self):
#         TODO: 
        return 3

a = Point(1,3)
b = Point(2,5)
c = a + b 
print(c)
# 
# 
# seg_1 = Segment(a,b)
# 
# print(seg_1)
# print('lenget of segment ',seg_1, ' is ', len(seg_1))

