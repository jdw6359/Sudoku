"""
Author: Josh Wooodward
Date: 8/13/13

Class is used to represent the current state of the board, and has methods
that assist in using the board directly

"""
class Board:
    
    def __init__ (self):
        #self.grid is 2x2 array
        self.grid=[[0 for j in range(10) ] for i in range(10)]
   
    def displayBoard(self):
        for i in self.grid:
            print(i)
            

