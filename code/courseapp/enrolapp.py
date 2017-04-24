from  pprint import pprint

    
def send_sms(student,msg):
    """awesome code to send sms"""
    phone = student.phone 
    
    print("sms send to num",msg,"---",phone)

def payment_gateway(card,amount):
    # do payment
    status = ['SUCCESS','FAILURE']
    import random
    status = random.choice(status)
    return status

    
def enroll_student(course,student):
#     pay the fees
    import random
    fee = course['fees']
    card = student['card']
   
    status = payment_gateway(card, fee)
    if status=='SUCCESS':
        course.add_student(student)
        
        print('welcome onboard')
        
    else:
        print('Payment failed')
        
        
def notify_student(course,msg):
    
    for student in course.students:
#         phonenumber = student['phone']
        send_sms(student, msg)
