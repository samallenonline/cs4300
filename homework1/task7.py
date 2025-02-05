# TASK 7: Package Control in DevEdu 
# objective - use pip package manager to add numpy and demonstrate 
# how to use the package to perform a specific function 

# run ```pip3 install numpy```
import numpy as np

# function that performs matrix multiplication using numpy arrays 
def matrix_multiplication():
    # create numpy arrays to use for multiplication
    matrix_a = np.array([[1,2], [3,4]])
    matrix_b = np.array([[5,6], [7,8]])

    # perform multiplication and save product matrix 
    matrix_c = np.dot(matrix_a, matrix_b)
    return matrix_c

# perform matrix multiplication using numpy 
if __name__ == "__main__":
    # verify numpy installation 
    print(np.__version__)

    # print product matrix 
    print(matrix_multiplication())