class A:
    def to_upper(self,name):
        
        self.name = name.upper()
    
    def title_name(self):
        self.title_name = self.name.title()
        
    def upper(self,name):

       upper_name = name.upper()

       upper_name = self.name.upper()

       
       return upper_name 
   
    
class B(A):
    def __init__(self,name):
        self.name = name 
    
a = B("sanjay")

a.upper.upper_name 


a.to_upper('ajay')
 
print(a.name)
print(a.title_name)
