import re 
# 1.) username: only lower chars, numbers, _

p =r"^[a-z0-9_]+$"

def valid_username(username):
    m  = re.match(p,username)
    return bool(m)


print(valid_username('sanjay'))
print(valid_username('sanj*ay'))