from shape import Path,Point
       
if __name__=="__main__":    
    p1 = Path()
    a1 = Point(0,0)
    p1.add(*[Point(*i) for i in [(1,3),(4,5),(6,7)]])
    
    
    print(p1.num_len())


