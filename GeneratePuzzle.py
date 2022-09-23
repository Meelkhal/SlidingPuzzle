# The following function generates a non sorted puzzle using RNG
# As a 3x3 array of integers
# 1 2 3
# 4 5 6
# 7 0 8
# The entry 0 will correspond to the blank space on the puzzle

# We're assuming the puzzle will be solved when the array corresponding to the image is given as follows
# 1 2 3
# 4 5 6
# 7 8 0
# As a result we need to consider an edge case to ensure that we don't try to solve a solved puzzle

#-Required Modules
import numpy as np

def GeneratePuzzle():
    elements = [0,1,2,3,4,5,6,7,8] # Elements in our sliding puzzle
    puzzle = np.ones((3,3)) # creates template for 3x sliding puzzle

    for i in range(3):
        for j in range(3):
            index = np.random.randint(len(elements))
            piece = elements.pop(index)
            puzzle[i][j] = piece
    
    return puzzle
