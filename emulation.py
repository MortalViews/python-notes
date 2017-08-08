class Point:
    def __init__(self,x,y):
        self.x = x 
        self.y=y
    
    def __add__(self,other):
        x1 = self.x+other.x
        y1=self.y+other.y 
        return Point(x1,y1)
        
    def __sub__(self,other):
        x1 = self.x-other.x
        y1=self.y-other.y 
        return Point(x1,y1)

    def __call__(self,*args):
        print('call was called')
        print(args)

class Points:
    def __init__(self):
        self.store = {}


    def __setitem__(self,k,p):
        print('set item called')
        self.store[k]=p
    
    def __getitem__(self,k):
        return self.store[k]
    
    
    def __contains__(self,k):
        return k in self.store
    
    
p1 = Point(1,2)

p1(1,2,4,5)


p = Points()

p['first_point']=p1

print(p['first_point'])

'first_point' in p 