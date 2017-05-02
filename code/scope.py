
name = 'test'
test = 'python'

def printr():
    age = 10
    test = 'algo'

def func():
    test = 'aws'
    def func1():
        
        def func2():
            print(test)
            print(name)
            print(len)
            
        return func2 
    
    return func1

t = func()
a = t()
b = a()
print(b)