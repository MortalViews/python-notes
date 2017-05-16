from pprint import pprint

# transaction=BANKACCOUNT


class BankAccount:
    bank_name = "ICICI"
    
    def __init__(self,customer_name,account_number):
        self.customer_name = customer_name.upper()
        self.account_number = account_number 
        self.balance = 0
    
#     @property 
#     def bankname(self):
#         return BankAccount.bank_name.upper()
    
    def deposit(self,amount):
        self.balance+=amount 
        
    def withdraw(self,amount):
        if amount>self.balance:
#             return "not sufficient balance"
            raise Exception("NOT SUFFICIENT BALANCE")
        old_balance = self.balance
        self.balance-=amount
        print("THE TRANSACTION ", old_balance,"-",amount,"=",self.balance)
        return self.balance

ac1 = BankAccount('sanjay','102029')
ac2 = BankAccount('ramesh','12292992')

ac1.deposit(100)
ac2.deposit(200)
ac1.withdraw(10)
ac2.withdraw(5)
print(ac1.balance)
print(ac2.balance)
