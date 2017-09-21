"""
Recall that the positions in a list of length n are 0,1,…,n-1.
 We want to write a function evenpositions(l) 
 that returns the elements at the even positions in l.
  In other words, the function should return the list [l[0],l[2],...].
   For instance evenpositions([]) == [], evenpositions([7]) == [7], 
   evenpositions([8,11,8]) == [8,8] and evenpositions([19,3,44,44,3,19]) == [19,44,3]. 
   A recursive definition of evenpositions is given below. You have to fill in the missing argument for the recursive call.def evenpositions(l):

"""

def evenpositions(l):
    print(l)
    if len(l) < 1:
         return []
    else:
        return evenpositions(l[2:]).append(l[0])

l = [8,11,8]
print(evenpositions(l))

x = 10
return('('+str(x))
    