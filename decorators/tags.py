def div(func):
    def  inner(*args,**kwargs):
        return "<div>"+func(*args,**kwargs)+"</div>"
    return inner

def title(func):
    def  inner(*args,**kwargs):
        return "<t>"+func(*args,**kwargs)+"</t>"
    return inner
def italics(func):
    def  inner(*args,**kwargs):
        return "<i>"+func(*args,**kwargs)+"</i>"
    return inner
def span(func):
    def  inner(*args,**kwargs):
        return "<span>"+func(*args,**kwargs)+"</span>"
    return inner
