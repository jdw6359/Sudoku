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
        self.read_write=FileCom()

    def configure_board(self,config_file):
        #prompt in future
        self.cur_file=config_file
        self.board=self.read_write.read(config_file)
        
    
