from pprint import pprint
t = [
    [1,2,4],
    [1,4,6],
    [7,4,6]
    ]
        
r = [ (i,j,elm) 
      for i,row in enumerate(t)
      for j,elm in enumerate(row)
      ]
pprint(r)
