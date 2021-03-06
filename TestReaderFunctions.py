"""
Test Suite for Reader Functionality
Author:Josh Woodward
Date: 8/21/13
"""

import unittest

from Sudoku import *

class TestReaderFunctions(unittest.TestCase):

    def setUp(self):
        sudoku=Sudoku()
        board_path="test_boards/test1.txt"
        sudoku.configure_board(board_path)
        self.board=sudoku.board

    def test_valueSet1(self):
        self.assertEqual(9,self.board.grid[0][0])
    
    def test_valueSet2(self):
        self.assertEqual(7,self.board.grid[2][3])

    def test_valueSet3(self):
        self.assertEqual(3,self.board.grid[8][7])

    def test_valueSet4(self):
        self.assertEqual(None, self.board.grid[3][2])

    def test_valueSet5(self):
        self.assertEqual(None,self.board.grid[7][8])

    def test_valueSet6(self):
        self.assertEqual(None,self.board.grid[5][3])


def Reader_Functions_Suite():
    tests=['test_valueSet1','test_valueSet2','test_valueSet3',
    'test_valueSet4','test_valueSet5','test_valueSet6']
    return unittest.TestSuite(map(TestReaderFunctions,tests))

if __name__=='__main__':
    suite=Reader_Functions_Suite()
    BasicRunner=unittest.TextTestRunner().run(suite)
        
