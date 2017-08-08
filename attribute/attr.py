class T:
    location="HYD"
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    
    
    def __getattr__(self,x):
        print('in get attr')
        l = x.lower()
        if l in self.__dict__:
          return self.__dict__[l]
        raise AttributeError()

    def __getattribute__(self,x):
        print('get attribute called')
        
    def __setattr__(self,n,v):
        pass 
t = T('sanjay',10) 

t.name = 'sanjay'
