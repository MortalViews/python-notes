
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
           break
        print(reminder)


prompt = 'Do you really want to do it?'

rv = ask_ok(prompt)

if rv: 
    print("YES! DONE")
else:
    print("Okay, will do it some other time !")