# The following function generates a non sorted puzzle using RNG
# As a 3x3 array of integers
# 1 2 3
# 4 5 6
# 7 0 8
# The entry 0 will correspond to the blank space on the puzzle

#-Required Modules
import numpy as np

def GeneratePuzzle():
    elements = [0,1,2,3,4,5,6,7,8] # Elements in our sliding puzzle
