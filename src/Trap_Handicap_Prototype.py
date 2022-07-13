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
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(funcName)s | %(message)s')

file_handler = logging.FileHandler(logfile)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.info("Logging started...")

# Calculator Class

class Calculator:
    def __init__(self) -> None:
        self.number_of_scores = args["scores"]
        self.max_average = 24.00
        self.average = None
        self.handicap = None
        #self.data_file = self.init_data
        if not isfile(args["file"]):
            open(args["file"], 'x')
        self.data_file = args["file"]
        self.scores = self.load_data(self.data_file)

    def __str__(self) -> str:
        if self.average != None or self.handicap != None:
            return f'Calculations({self.average}, {self.handicap})'
        else:
            return "No Calculation"

    def load_data(self, data_file) -> dict:
        try:
            file = open(data_file, 'r')
        except OSError as e:
            logger.exception("Failed to read file " + str(data_file))
            print("Failed to read file " + str(data_file))
            sys.exit()
        data = json.load(file)
        logger.info("Data loaded...")
        return data

    def sort_data(self) -> None:
        pass

    def calculate_average(self, scores: tuple) -> None:
        if len(scores) < self.number_of_scores:
            # If there are less than
            self.average = 0
            logger.debug("The number of scores to calculate the average was less than number of scores to be used to calculate")
        else:
            # Calculate the average
            self.average = sum(scores) / len(scores)

    def calculate_handicap(self) -> None:
        if self.average > self.max_average:
            self.handicap = 0
        else:
            h = self.max_average - self.average
            self.handicap = round(h)

    def write_to_file(self, new_data: dict) -> None:
        with open(self.data_file, 'r+') as file:
            file_data = json.load(file)
            file_data['Scores'].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent=4)

if __name__ == '__main__':
    calc = Calculator()
    print(calc)
