class Point:
    name ="Point class"
    
    def __init__(self,x,y):
        print(self)
        self.x = x 
        self.y = y
        
    def cal_area(self):
        self.area =self.x*self.y 
         
         
a = Point(1,2)
b = Point(3,17)
          

a.cal_area()
print(a.area)
print(b.area)
