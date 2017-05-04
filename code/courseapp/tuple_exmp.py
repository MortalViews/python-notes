from pprint import pprint
def func():
    pass
class T:
    pass

t = (1,'sanjay',[],func,T,T(),func())
pprint(t)
a = t[2]
print(a)