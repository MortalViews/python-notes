from util import print_full_name

class Person:
    pass   

class Student:
    def echo(obj):
        return obj
#         print("full name is: "+obj.first_name+' '+obj.last_name)

rv = Student.echo(1)
# s = Student()
print(rv)

print(Student.echo('sanjay'))
# 
s = Student()
rv = s.echo()
print(rv)

