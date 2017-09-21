"""
1.) find all lowercase letters in a string
2.) validate username:
only lowercase, digists and underscore
3.) replace every charector in a string with another char
"""

import re 

p1 = r"[a-z]"

s1 ="aDududaauXudffhfd197272xycy"

r1=''.join(re.findall(p1,s1))
print(r1)


def valid_username(username):
    p2=r"^[a-z_\d]+$"
    return bool(re.match(p2,username))

print(valid_username('sdsdo'))


def is_even(i):
    return i%2==0

l = list(range(10))
print(l)

r = list(filter(is_even,l))

l = [0,1,None,1,2,3,5]
print(list(filter(None,l)))

