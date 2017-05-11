import time 
import threading
from threading import Thread
import random
import types
def random_sleep():
    return random.randint(1,5)
def mock_long_task(msg,sleep=2,nums=5):
    print(msg)
    ct = threading.current_thread().name
    s =  (lambda : sleep())if hasattr(sleep,'__call__') else (lambda : sleep)
    while nums > 0:
        r = s()
        print(msg+'...time left..'+str(r)+"..."+str(nums)+ct)
        time.sleep(r)
        nums=nums-1
class MockPaymentGateway:
    def __init__(self,msg):
        pass 
    
class PaymentGateway():
    def make_payment(self,sleep=2,nums=5):
        mock_long_task("making..payment..",nums,sleep=sleep)
        print("..making payment")
        time.sleep(3)
t = PaymentGateway()
th1 = threading.Thread(target=t.make_payment)
th2 = threading.Thread(target=t.make_payment,kwargs={'sleep':random_sleep})
th1.start()
th2.start()

