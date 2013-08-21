#import each of the test files
from unittest import *

from TestBasicFunctions import *
from TestValidationFunctions import * 


#initizlize array of suites
suite_array=[]

#create a suite for each test file
suite_array.append(Basic_Functions_Suite())
suite_array.append(Validation_Functions_Suite())



#run each suite
for suite in suite_array:
    
    BasicRunner=unittest.TextTestRunner().run(suite)
