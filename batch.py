from argparse import ArgumentParser
from billcal import (PriceCalulator,
                                read_from_file,
                                write_solutions_to_files)

pc = PriceCalulator(ing_max_price=40,
                    ing_min_price=1)

if __name__=="__main__":
    parser = ArgumentParser("price calculator")
    parser.add_argument('--input','-i',type=str,required=True)
    parser.add_argument('--output','-o',type=str,default=None)
    
    
    args = parser.parse_args()
    input_file = args.input
    data = read_from_file(input_file)
    
    for dish in data:
        pc.add_dish(dish)
    
    write_solutions_to_files(output_path=args.output,
                             solutions=pc.solutions)