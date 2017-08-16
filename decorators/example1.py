class User:
    def __init__(self,name,permissions):
        self.name = name 
        self.permissions = permissions

def can(permission):
    return permission in current_user.permissions 

    

def requires(permission):
    def inner(f):
        def decorated(*args,**kwargs):
            if not can(permission):
                raise Exception("FORBIDDEN")
            return f(*args,**kwargs)
        return decorated
    return inner 



@requires('CAN_DELETE')
def delete_post():
    print('delting post')
    

delete_post = requires("CAN_DELETE")(delete_post) 

delete_post() 

@requires("CAN_ADD")
def add_post():
    print("adding post")
    
@requires(['VIEW_POST'])
def view_post():
    pass 
current_user = None 

u1 = User("sanjay",['CAN_DELETE'])
u2=User("raj",['CAN_ADD'])    


current_user = u2
add_post()