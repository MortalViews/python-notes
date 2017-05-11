import time
import random
import datetime 
from numpy import bench
from functools import wraps
def benchmark(func):
    @wraps(func)
    def _inner(*args,**kwargs):
        now = datetime.datetime.now()
        rv = func(*args,**kwargs)
        later = datetime.datetime.now()
        total_exec_time = (later - now).total_seconds()
        print("function. %s took:  %s seconds"%(func.__name__,str(total_exec_time)))
    return _inner
 
def random_seconds():
   return random.randint(1,5)

class A:
   def _do_task(self):
       seconds = random_seconds()
       time.sleep(seconds)
   
   do_task = benchmark(_do_task)
   
   
class B:
    def _do_another_task(self):n
       seconds = random_seconds()
       time.sleep(seconds)
    
    do_another_task = benchmark(_do_another_task)
    
def _run_task():
   a = A()
   a.do_task()
   b = B()
   return b.do_another_task


run_task = benchmark(_run_task)
a = A()
a.do_task()

b = B()
b.do_another_task()


# 
# 
# 
# 
# next_task = benchmark(run_task)
# # next_task = run_task()
# next_task()
# b = B()
# # now = datetime.datetime.now()
# rv = benchmark(b.do_another_task)
# 
# # later = datetime.datetime.now()
# # total_exec_time = (later - now).total_seconds()
# # 
# # print(total_exec_time)
# 
# run_task()
# print('completed')
