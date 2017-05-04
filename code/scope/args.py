def cap_print(*names):
    n = []  
    for i in names:
        i.upper()
        n.append(i)
    
    return tuple(n)
    
#     return a1.upper()

def title_print(name):
    return name.title()


def test1(func):
    f = func
    def test2(*args):
        return f(*args)
    return test2

a = test1(cap_print)

b = test1(title_print)

a1 = a('sanjay','deepkar')
print(a1)

print(a('sanjay'))
print(a('te','t','a'))






