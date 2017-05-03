# Local scope 
# Enclosed Scope 
# GLobal 
# Buidin

name = 'test'
test = 'python'

def printr():
    age = 10
    test = 'algo'

def func():
    test = 'aws'
    def func1():
        def len():
            prin('len called')
        def func2():
            print(test)
            print(name)
            print(len)
            
        return func2 
        func2()
    return func1

func1 = func()
func2 = func1()


b = func2()
print(b)