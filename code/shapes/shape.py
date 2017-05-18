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
        

