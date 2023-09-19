import os
import argparse # to give command line input
import yaml # to read the yaml files(these files are where we define the configurations)
import logging # for logging all the info (we can also use print statement but using logging is the standard)






if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="default")
    args.add_argument("--datasource",default=None)

    parsed_args=args.parse_args()
    print(parsed_args.config, parsed_args.datasource)

