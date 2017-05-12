import time 
import threading
from threading import Thread
import random
import types

def random_sleep():
    return random.randint(1,5)
        
class MockTask(Thread):
 
    def __init__(nums,seconds):
        self._nums=wrap_func(nums)
        self._seconds = wrap_func(seconds)

    @property 
    def nums():
        return self._nums()
    
    @property 
    def seconds:
        return self._seconds() 
    
    def step(seconds,nums):
        pass
        
    def start():
        self.mock()
        
    @property    
    def id():
        return threading.current_thread.name
    
    def mock()
        nums = self.nums 
        while nums > 0:
            seconds = self.seconds()
            time.sleep(seconds)
            self.step(seconds,nums)
            nums=nums-1
            
def wrap_func(func):
    return func if hasattr(func,'__call__') else  lambda: func

class VisaPaymentGateway(MockTask):
    
    def __init__(seconds,nums):
        MockTask.__init__(seconds,nums)
        self.msg = "vis payment...running."
        
    def step(seconds,nums):
       print(self.msg+" ...nums "+ nums+"id: "+self.id)
        
    
