"""
Test Suite for Writer Functionality
Author:Josh Woodward
Date: 8/21/13
"""

import unittest

from Sudoku import *

class TestWriterFunctions(unittest.TestCase):

    def setUp(self):
        #set up board
        self.sudoku=Sudoku()
        board_path="test_boards/test1.txt"
        self.sudoku.configure_board(board_path)
        self.board=self.sudoku.board




        #assert value on board

        #change board

        #write board

        #open board

        #assert value has changed

    def test_test1(self):
        pass
    
def Writer_Functions_Suite():
    tests=['test_test1']
    return unittest.TestSuite(map(TestWriterFunctions,tests))

if __name__=='__main__':
    suite=Writer_Functions_Suite()
    BasicRunner=unittest.TextTestRunner().run(suite)
    


    
        
