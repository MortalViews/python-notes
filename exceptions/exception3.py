
class InvalidValue(ValueError):
    pass 

def add(x,y):
    if not  isinstance(x, int):
        raise InvalidValue("invalid value for x")
    if not  isinstance(y, int):
        raise InvalidValue("invalid value for y")
   
    return x+y




print(add(1,'a'))


