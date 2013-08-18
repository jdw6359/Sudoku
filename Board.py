"""
Author: Josh Wooodward
Date: 8/13/13

Class is used to represent the current state of the board, and has methods
that assist in using the board directly 

"""
class Board:
    
    def __init__ (self):
        #self.grid is 2x2 array
        self.grid=[[None for j in range(10) ] for i in range(10)]
   
    """
    used to set the given row and col's value
    """
    def setValue(self,row,col,value):
        
        self.grid[row][col]=value

    """
    given a row and a value, will loop through cols of that row
    and check for matches. If matched, move is invalid and
    bool invalid=true
    """
    def horizontal_validation(self,row,value):
        invalid=False
        col=0
        while(col<9):
            if self.grid[row][col]==value:
                invalid=True
            col+=1
        return invalid

    """given a column and a value, will loop through rows of that col
    and check for matches. If matched, move is invalid and
    bool invalid=true
    """
    def vertical_validation(self,col,value):
        invalid=False
        row=0
        while(row<9):
            if self.grid[row][col]==value:
                invalid=True
            row+=1
        return invalid


    
    """
    Simply displays the board
    """
    def displayBoard(self):
        top=""
        for i in range(0,9):
            for j in range(0,9):
                if self.grid[i][j]==None:
                    value=" "
                else:
                    
                    value=str(self.grid[i][j])
                top+=value
                top+=" "
                if j==2 or j==5:
                    top+="| "
            top+="\n"
            if i==2 or i==5:
                top+="---------------------\n"
        print(top)
            

            

