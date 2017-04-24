
class FrontDesk():
    
    def __init__(self):
        pass
    
    def get_courses(self):
        """
        Provide all available courses 
        """
        return 
    
    def enroll(self,course,student):
        
#         made payment
        course.add_student(student)
class Card():
    def __init__(self,name,number,type):
        self.person_name=name 
        self.card_number = number 
        self.type = type 
               
class PaymentGateway():
    def __init__(self,provider_name):
        self.name = provider_name
    
    def pay_by_dd_card(self):
        pass  
    def pay_by_cc_card(self):
        pass 
    def pay_by_wallet(self):
        pass
    def pay_by_netbanking(self):
        pass 
    def pay_by_card(self,card):
        pass 
    
    
class Faculty():
    def __init__(self,name,age,phone):
        self.name = name 
        self.age = age 
        self.phone = phone 

class Student():
    
    def __init__(self,name,age,phone,card):
        self.name = name 
        self.age = age 
        self.phone = phone 
        self.card = card
        
    def __repr__(self):
        return "<name: %s  age: %s>"%(self.name,self.phone)
    
class Course():

    def __init__(self, name, faculty, room, time, fees,students=[]):
        self.name = name
        self.faculty = faculty
        self.room = room
        self.time = time
        self.students = students 
        self.fees = fees 

    
    
    def add_student(self,student):
        self.students.append(student)
        
