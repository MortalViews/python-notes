
name = 'sanjay'

def test(x):
    name = x
    def test1(y):
        name = y
        def set_name(n):
            nonlocal name
            name = n
            
        return set_name
    
    def print_name():
        print(name)
        
    return test1,print_name 
    
t,print_t = test('ajay')
print_t()
x = t('deepak')
x('ramu')
print_t()
