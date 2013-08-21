"""
Test Suite for Board Validation Functionality
Author:Josh Woodward
Date: 8/21/13
"""

import unittest

from Board import *

class TestValidationFunctions(unittest.TestCase):


    def setUp(self):
        self.board=Board()
        #fill the board with values that will
        #make for both valid and invalid situations
        self.board.setValue(0,0,4)
        self.board.setValue(0,1,5)

    def test_horizontal1(self):
        self.assertTrue(self.board.horizontal_validation(0,6))

    def test_horizontal2(self):
        self.assertFalse(self.board.horizontal_validation(0,4))
    
def Validation_Functions_Suite():
    tests=['test_horizontal1','test_horizontal2']
    return unittest.TestSuite(map(TestValidationFunctions,tests))

if __name__=='__main__':
    suite=Validation_Functions_Suite()
    BasicRunner=unittest.TextTestRunner().run(suite)
