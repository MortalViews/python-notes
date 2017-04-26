# name = 'sanjay'
nums = []
print(id(nums))

def num_appender(a,l=[]):
    print(id(l))
    l.append(a)
 


num_appender(1)