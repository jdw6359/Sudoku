"""
Author: Josh Woodward
Date: 8/15/13

Class that will be used for file I/O
"""
from Board import * 

class FileCom:

    def __init__(self):
        pass

    """
    will configure and return a board object
    based on file_path
    """
    def read(self, config_file):
        config=open("ConfigFiles/"+config_file)
        board=Board()
        row=0
        col=0
        for line in config:
            for item in line:
                if item !="\n":
                    if item != ".":
                        board.setValue(row,col,item)
                    col+=1
                 
                
                
                    
            row+=1
            col=0
        return board
    
            
        
        
