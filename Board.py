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
        top=""
        for i in range(0,9):
            for j in range(0,9):
                top+=str(self.grid[i][j])
                top+=" "
                if j==2 or j==5:
                    top+="| "
            top+="\n"
            if i==2 or i==5:
                top+="---------------------\n"
        print(top)
            

            

