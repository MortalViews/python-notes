class A:
    def calculate_commission(self,amount,percent=None):
        if not percent: 
            percent = self.percent
        return (percent*amount)/100
     
def x(percent,age =80, score=10):
    if age > 100:
        if score == 10:
            percent = percent/5
            
    percent = age/10
    return percent

class B(A):
    
    def __init__(self,percent=2):
        self.percent=percent
    def c(self,percent):
        self.percent = percent
    
agent= B(3)
worker = B()
amount = 100
agent.c(14)

x.percent = 12
x.name = 'tododod'
# x(10)

print(A.calculate_commission(x, amount))


print(agent.calculate_commission(amount))



