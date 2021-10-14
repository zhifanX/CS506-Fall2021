import numpy as np

def get_determinant(matrix):
    """
    input: a matrix (list of lists)
    returns: the determinant of the matrix
    """    
    #check if input is a valid n*n matrix
    if (len(matrix) != len(matrix[0])):
         raise ValueError('input matrix is not valid')
    if (len(matrix) <= 0):
        return None
    elif (len(matrix) == 1):
        determint = matrix[0][0]
        return determint
    else:    
        determint = 0.0
        for col in range(len(matrix)):
            sub_matrix = matrix.copy()
            sub_matrix = np.delete(sub_matrix, col, axis = 1)
            #delete the first row
            sub_matrix = np.delete(sub_matrix, 0, axis = 0)
            determint += matrix[0][col] * ((-1) ** (col % 2)) * get_determinant(sub_matrix)
    return determint