import time
import datetime 

def benchmark(func):
    start = datetime.datetime.now()
    func()
    end = datetime.datetime.now()
    exec_time = (end- start).total_seconds()
    print('executing_really_complex',int(exec_time))

def test1():
#some complex process
    time.sleep(2)
    test2()
    test2()
def test2():
    #some complex process
    time.sleep(3)
def test3():
    t = T()
    t.really_complex()
    
class T:
    def really_complex(self):
        time.sleep(4)
        
benchmark(test1)
test1()
test2()
