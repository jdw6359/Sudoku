#import each of the test files
from TestBasicFunctions import *


#initizlize array of suites
suite_array=[]

#create a suite for each test file
suite=Basic_Functions_Suite()
suite_array.append(suite)



#run each suite
for suite in suite_array:
    
    BasicRunner=unittest.TextTestRunner().run(suite)
