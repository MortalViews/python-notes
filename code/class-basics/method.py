class Student:
    course = 'aws-01'
    grade='05'
    
    def __init__(self,name,age,address):
        self.name =name
        self.age = age
        self.full_name = self.name.upper()+' '+str(self.age)*20
        
        
    def say_hi(self,to,frm):
        return "Hi "+self.name+' '+to+' '+frm

s = Student('sanjay',10,'long address')



class Method():
    def __init__(self,func,obj):
        self.func = func 
        self.obj = obj
        
    def __call__(self,*args):
        args = list(args)
        args.insert(0,self.obj)
        
        return  self.func(*args)

m1 = s.say_hi('a','b')
      
print(m1('a','b'))

m2 = Method(Student.say_hi,s)
print(m2('a','b'))









