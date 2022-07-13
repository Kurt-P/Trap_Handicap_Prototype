import sys
from os import mkdir, getpid
from os.path import isfile, isdir
import json

class Player:

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name: str, data_source) -> None:
        self.name = name
        self.data_source = data_source
        self.handicap = self.load_average_from_file(self.data_source)

    def load_average_from_file(self, data_file) -> None:
        try:
            file = open(data_file, 'r')
        except OSError as e:
            #logger.exception("Failed to read file " + str(data_file))
            print("Failed to read file " + str(data_file))
            sys.exit()
        data = json.load(file)
        #logger.info("Data loaded...")
        #return data
        player_data = data['Handicaps']['Person' == self.name]
