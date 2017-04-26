def init(obj,name,age):
    obj.name = name 
    obj.age = age
    

class Human:
    def __init__(self):
        print(type(self))

class Person(Human):
    def full_name(self):
        return "full name is: "+self.first_name+' '+self.last_name
        
class Faculty(Person):
    def __init__(self,name,age,phone):
        self.laptop
    def take_class(self):
        pass
    def project_screen(self):
        pass

class Student(Person):
    
    def take_notes(self):
        pass 
    
    def ask_doubts(self):
        pass 
   


        