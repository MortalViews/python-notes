# sum of diagonal elements 
# sum of each columns
# sum of each row 
# total sum 

t = [
    [1,2,4],
    [2,4,5],
    [2,4,5]
    ]

diag=[]
for i,row in enumerate(t):
    print(i,row)
    for j,elm in enumerate(row):
       if i == j:
           diag.append(elm) 
           
diag = [ elm for i,elm in enumerate(row)
             for i,row in enumerate(t)
              if i==j ]           
print(sum(diag))
 

