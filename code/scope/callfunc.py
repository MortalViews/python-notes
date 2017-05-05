import test
def test1(value):
    def test2():
        def test3():
            return value
        return test3
    return test2


v = test1('sanjay')()()

def get_user_name():
    return 'sanjay'

def title(x):
    return x.title()

def hi(z):
    return "HI %s,"%z

def welcome(y):
    return y+"Welcome"

def goodbye(z):
    return z+"Good Bye"

wecome_message = welcome(hi(title(get_user_name())))
good_bye = goodbye(hi(title(get_user_name())))

print(wecome_message)
print(good_bye)