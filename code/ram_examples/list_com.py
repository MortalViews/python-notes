matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
t = [ [row[i] for row in matrix] for i in range(4) ]


l = []

for i in range(4):
    x = []
    for row in matrix: 
        x.append(row[i])
    l.append(x)
    
    
print(l)


# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]