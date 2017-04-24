from pprint import pprint


from student import students 
from enrolapp import enroll_student
from entity import Student,Course
from enrolapp import notify_student

aws_course = Course(name='aws_101',
                    faculty='john',
                    room='1A',
                    time='7.30',
                    fees='1000')

for s_details in students: 
    
    student = Student(**s_details)
    
    aws_course.add_student(student)


pprint(aws_course.students)


notify_student(aws_course,'The class starts in 5')























