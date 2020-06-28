import argparse
import pandas as pd 
from src.funcs import *


parser = argparse.ArgumentParser()
parser.add_argument('-y','--year', type=int, help="WC year for analysis")
parser.add_argument('-p','--position', type=int, help="Position for analysis")
args = parser.parse_args()

def main():
    checkerror(args.year,args.position)
    wc_matches_clean = pd.read_csv('./Input/wc_data.csv',index_col=0)
    matches_filter = filter_data(wc_matches_clean,args.year,args.position)
    print(matches_filter)



if __name__ == '__main__':
    main()