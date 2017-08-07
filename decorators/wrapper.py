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

"""
say_hi=tag('html')(tag('p')(tag('t')(tag('span')(say_hi))))
"""
