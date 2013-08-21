"""
Test Suite for basic functionality
Author: Josh Woodward
Date: 8/21/13
"""

import unittest


from Board import *


class TestBasicFunctions(unittest.TestCase):

    #creates an empty board
    def setUp(self):
        self.board=Board()


    #Ensures each slot in a fresh grid is occupied with None
    def test_clear(self):
        for row in range(9):
            for col in range(9):
                self.assertEqual(None,self.board.grid[row][col])

    #Ensures that a value is added to a specific row,col
    def test_add1(self):
        self.board.setValue(1,1,4)
        self.assertEqual(4,self.board.grid[1][1])

    #Ensures that a value is added to a specific row,col
    def test_add2(self):
        self.board.setValue(7,5,4)
        self.assertEqual(4,self.board.grid[7][5])

    #Ensures that an added value is removed from the specific row,col
    def test_remove1(self):
        self.board.setValue(1,1,4)
        self.assertEqual(4,self.board.grid[1][1])
        #will remove and assert None
        self.board.removeValue(1,1)
        self.assertEqual(None,self.board.grid[1][1])

    #Ensures that an added value is removed from the specific row,col
    def test_remove2(self):
        self.board.setValue(7,5,4)
        self.assertEqual(4,self.board.grid[7][5])
        #will remove and assert None
        self.board.removeValue(7,5)
        self.assertEqual(None,self.board.grid[7][5])
    

def Basic_Functions_Suite():

    tests=['test_clear', 'test_add1','test_add2','test_remove1','test_remove2']
    return unittest.TestSuite(map(TestBasicFunctions,tests))

if __name__ =='__main__':

    suite=Basic_Functions_Suite()
    BasicRunner=unittest.TextTestRunner().run(suite)

    #unittest.main()

