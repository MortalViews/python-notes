
def cap_print(*names):
    print(type(names))
    print(names)
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

