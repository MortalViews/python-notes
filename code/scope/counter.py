
def counter(start=0,step=1):
    def inner():
        nonlocal start
        start= start+step
        return start
    return inner


oddcounter = counter(start=10,step=2)

evencounter = counter(start=2)

print(oddcounter()) #12
print(oddcounter()) #12 14 
print(oddcounter()) #12 16 

print(evencounter())
print(evencounter())
print(evencounter())