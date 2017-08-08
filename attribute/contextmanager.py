class T:
    def __enter__(self):
        print('entered')
        return '1'
        
        
    def __exit__(self,exc_type, exc_value, traceback):
        print('exit called')
        
        
        
        
t  = T()

with t as x:
    print(x)
    
    
print('outide')
        
        
     
    
    