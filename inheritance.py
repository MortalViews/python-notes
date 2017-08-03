import random
class Person:
    def __init__(self,name,age,location):
        self.name = name 
        self.age = age 
        self.locaiton = location

    def is_sick(self):
        return random.randint(1,10)%2==0
    
class AttendenceMixin:
    def swip_in(self):
        pass 
    def swip_out(self):
        pass 
class Employee(Person):
    def __init__(self,emp_id,joining_date,*args,**kwargs):
        self.emp_id =emp_id
        self.joining_date =joining_date
        super().__init__(*args,**kwargs) 
        
class Contractor(Employee):
    pass 

class InfraEmployee(Employee,AttendenceMixin):
   def __init__(self,dept,*args,**kwargs):
       self.dept = dept
       super().__init__(*args,**kwargs) 
       
class ITEmployee(Employee,AttendenceMixin):
    def __init__(self,project,technologies,system_id,*args,**kwargs):
        self.project =project
        self.tech = technologies
        self.system = system_id
        super().__init__(*args,**kwargs)
    
    def is_sick(self):
        return random.randint(1,10)%2==1
    
class Manager(Employee):
    def __init__(self,cabin_no,*args,**kwargs):
        self.cabin=cabin_no
        super().__init__(*args,**kwargs)

