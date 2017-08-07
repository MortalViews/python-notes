name='sanjay'
def log(func):
    def inner(*args,**kwargs):
        print('func called..')
        r = func(*args,**kwargs)
        print('func call end')
        return r
    return inner 

def title(func):
    def inner(*args,**kwargs):
        r = func(*args,**kwargs)
        return "<t>"+r+"</t>"
    return inner 

def bold(func):
    def inner(*args,**kwargs):
        r = func(*args,**kwargs)
        return "<b>"+r+"</b>"
        
    return inner 

def tag(tag_name):
    def inner_1(func):
        def inner_2(*args,**kwargs):
            value = func(*args,**kwargs)
            return "<"+tag_name+">"+value+"<"+tag_name+"/>"
        return inner_2
    return inner_1 




@tag('html')
@tag('p')
@tag('t')
@tag('i')
@tag('span')
def say_hi(name):
    return "HI %s"%(name)


print(say_hi('sanjay'))