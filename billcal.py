from pprint import pprint
from argparse import ArgumentParser
import csv
import os 
import shutil

default_output_loc=os.path.join(
                    os.path.dirname(os.path.dirname(os.path.dirname((__file__)))),
                    'solutions')  


class PriceCalulator:
    def __init__(self,ing_min_price,ing_max_price):
        self.solutions=[]
        self.is_first=True
        self.ing_min_price = ing_min_price
        self.ing_max_price = ing_max_price
    
    def start_end_price(self,price):
        if price<=self.ing_max_price:
            return 1,price-1
        else:
            s=price-self.ing_max_price
            e=self.ing_max_price
            return s,e

    def add_first_dish(self,dish):
        self.is_first=False
        x,y,v = dish
        s,e = self.start_end_price(v)
        self.solutions=[{x:i,y:v-i} for i in range(s,e+1)]
  
    def add_dish(self,dish):
        if self.is_first:
            return self.add_first_dish(dish)
        x,y,v = dish
        new_solutions=[]
        #max 40
        for s in self.solutions:
            if x not in s and y not in s:
                raise RuntimeError("invalid dish (%s,%s,%d)"%(x,y,v))
            if x not in s:
                #so that x is always the known ingr
                y,x=x,y
            v1 = v-s[x]
            if 0<v1<41:
                s[y]=v1
                new_solutions.append(s)
        self.solutions=new_solutions
    
    def parse_data(self,file_path):
        with open(file_path,'r') as f:
            reader = csv.reader(f,delimiter=',')
            #don't want header
            next(reader)
            for x,y,v in reader:
                yield x.strip(),y.strip(),int(float(v.strip('$ ')))

    def add_from_file(self,file_path):
        for dish in self.parse_data(file_path):
            self.add_dish(dish)
    
    def print_solutions(self):
        for i,s in enumerate(self.solutions):
                i+=1
                print('-'*20)
                print("solution %i:"%(i))
                print('-'*20)
                print('%s,%s'%("Ingredient","Price"))
                for k,v in s.items():
                    print('%s,$%.2f'%(k,float(v)))
    
    def write_solutions(self,output_path=None):
        if not output_path:
            output_path = default_output_loc
        output_path = os.path.expanduser(output_path)    

        if os.path.exists(output_path):
            shutil.rmtree(output_path)
        os.mkdir(output_path)
    
        print('writing output to %s'%(output_path))
        
        for i,s in enumerate(self.solutions):
            with open(os.path.join(output_path,str(i)),'w') as o:
                o.write('%s,%s\n'%("Ingredient","Price"))
                for k,v in s.items():
                    o.write('%s,$%.2f\n'%(k,float(v)))

