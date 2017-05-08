
name = 'sanjay'

def test(x):
    name = x
    def test1(y):
        name = y
        def print_name():
            global name
            print(name)
        return print_name
    
    def print_name():
        print(name)
        
    return test1,print_name 




rv = test('ajay') 
# t,print_t = test('ajay')

print_t()
x = t('deepak')

x()

