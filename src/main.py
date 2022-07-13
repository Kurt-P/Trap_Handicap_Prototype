from calculator import Calculator

import sys
import argparse
from os import mkdir, getpid
from os.path import isfile, isdir
import logging
import json
from datetime import date

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--date", required=False, default=date.today(),
                help="The date for which the score was shot")
ap.add_argument("-f", "--file", required=False, default="Scores.json",
                help="Specify the file to be used")
ap.add_argument("-p", "--person", required=False,
                help="The person who's score is being recorded")
ap.add_argument("-s", "--scores", required=False, type=int, default=3,
                help="Use the last number scores to calculate the average")
ap.add_argument("-v", "--verbose", required=False, type=bool, default=False,
                help="Set the verboseness of the coordinator.")

args = vars(ap.parse_args())

if not isdir("./logs"):
    try:
        mkdir("./logs")
    except Exception as e:
        print("Failed to make log dir")

logfile = './logs/TrapHandiCap.log'

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(funcName)s | %(module)s | %(message)s')

file_handler = logging.FileHandler(logfile)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.info("Logging started...")

if __name__ == '__main__':
    calc = Calculator()
    print(calc)
