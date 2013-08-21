"""
Author:Josh Woodward
Date: 8/21/13

Class that will be used to represent the game as a whole
"""
from Board import *
from FileCom import * 


class Sudoku:

    #add more variables here that will be used to represent the current game
    def __init__(self):
        self.reader=FileCom()

    def configure_board(self,config_file):
        #prompt in future
        self.board=self.reader.read(config_file)
    
