t = range(100)

r = []
for i in t:
    if i>5:
        r.append(i)
        
        
r = [i for i in t if i > 30 and i%2!=0]
print(r)