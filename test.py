from pprint import pprint
from inheritance import Employee,ITEmployee
# e1 = Employee(
#     name='sanjay',
#     age = 10,
#     location='hyd',
#     emp_id=1000,
#     joining_date='2016-10-10',
#     )


i1=ITEmployee(
    project='s1',
    technologies=['java'],
    system_id = 10,
    name='sanjay',
    age = 10,
    location='hyd',
    emp_id=1000,
    joining_date='2016-10-10'
    )


print(i1.is_sick())