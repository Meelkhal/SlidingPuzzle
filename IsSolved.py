# The following function checks to see if a puzzle is solved
# Input: 3x3 array of INTs
# Checks to make sure that the array is equivalent to 
# 1 2 3
# 4 5 6
# 7 8 0
# Which is a solved sliding puzzle
import numpy as np

def IsSolved(puzzle):
    # Checks the equality of two arrays
    solved = np.array([[1,2,3],[4,5,6],[7,8,0]])
    check = solved == puzzle
    equality = check.all()
    return equality
