import time 


class Person:
    
    def __init__(self,name):
        self.name = name
        
    def greet(self):
        print("HI, i am %s ! how are you today!"%self.name)
        
class Cashier(Person):
    def accept_payment(self):
        print("accepting payment")
        
    def print_bill(self):
        i=0
        while i > 3:
            print('printing bill')
            time.sleep(1)
            i=+1
class Store:
    def __init__(self,address,salesman,cashier):
        self.address = address 
        self.salesman = salesman 
        self.cashier = cashier 
    def attend_customer(self):
        self.salesman.sell()  
    

class SalesMan(Person):
#     def __init__(self):
#         
#         pass 
#     
    def take_order(self):
        i=0
        while i>3:
            print('taking order..')
            time.sleep(1)
            i=+1
    
    def sell(self):
        self.take_order()
        self.store.cashier.accept_payment()
     
class Adresss:
    def __init__(self,line1,line2,landmark,contact):
        self.line1 = line1 
        self.line2 = line2 
        self.landmark = landmark
        self.contact = contact 

my_store_address = Adresss('line1 address','line2 address','test lankdarmd','10292929')
my_salesman = SalesMan()
# my_salesman.greet()
# my_store =Store("this is an address")
