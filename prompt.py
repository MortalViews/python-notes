from pprint import pprint
from billcal import PriceCalulator

pc = PriceCalulator(ing_max_price=40,
                    ing_min_price=1)
try: 
    #to work with 2.7 raw_input
    input = raw_input
except:
    pass

while True:
    i = input("Enter Option: 1 -> add new dish,2 -> show_solutions,3 -> write to file\n")
    if i=='1':
        x,y,v = input("Enter Dish in ing1,ing2,price format:\n").split(',')
        v = int(float(v.lstrip('$')))
        pc.add_dish((x,y,v))
    elif i=='2':    
        pc.print_solutions()
        
    elif i =='3':
        output = input("Enter output path: ")
        pc.write_solutions(output)
    else:
        print("invalid input")