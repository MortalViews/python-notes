class A:
    def __init__(self,name1):
        self.name = name1
        


class B(A):
    
    def __init__(self,percent=2):
        self.percent=percent
    def c(self,percent):
        self.percent = percent
    

b = B()

print(b.__init__)