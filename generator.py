from pprint import pprint

def gen(n):
    for i in range(n):
        yield i*i
        
    print('for loop completed')
    
t = gen(10)


for i in t:
    print(i)
