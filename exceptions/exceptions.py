
def add(x,y):
    return x+y 


input =[(1,2),(1,6),('a',1),(1,7)]


result = {}
for i in input:
    try:
       
        t=r
        result[i]=add(*i)
       
    except Exception as e:
        print('i got an error for'+str(i))
        print(str(e))

print(result)



    