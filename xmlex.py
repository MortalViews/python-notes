import os 
from pprint import pprint
import xmltodict
base_dir = '/home/sanjay'
path = os.path.join(base_dir,'w3.xml')
print(path)
with open(path) as fd:
    doc = xmltodict.parse(fd.read())
    pprint(doc['breakfast_menu'])
    
    

           
           
           


