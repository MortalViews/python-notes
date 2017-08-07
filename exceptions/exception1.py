
def throws_error():
    raise TypeError()

def some_func():
    throws_error()

def some_handler():
    try:
        print("")
        some_func()
        print("")
    except TypeError as e:
        print("eror happened: "+str(e))
        raise IndexError("some index error") 
    except AttributeError as e:
        print("eror happened: "+str(e)) 
    except OSError as e:
        print("i got OSError")
        
def call_handler():        
    try:
        some_handler()
    except IndexError as e:
        print("got index error")
        print(str(e))
    except TypeError:
        print('got type error')
        
    

call_handler()

"""
call_handler
 --some_handler 
   -- some_funcs 
      -- throws error
"""