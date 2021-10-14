import numpy as np
import sys
sys.path.insert(0,'/Users/x/CS506-Fall2021/02-library')
from cs506 import matrix

def test_2x2_pos():
    arr = np.array([[1,3],[9,10]])
    expected = np.linalg.det(arr)
    test = matrix.get_determinant(arr)
    print(expected)
    print(test)
    assert expected == test

def test_3x3_pos():
    arr = np.array([[1,2,3],[9,10,11],[20,21,22]])
    expected = np.linalg.det(arr)
    test = matrix.get_determinant(arr)
    print(expected)
    print(test)
    assert expected == test

def test_4x4_neg():
    arr = np.array([[-1,-2,-3,-4],[-9,-10,-11,-12],[-20,-21,-22,-23],[-55,-56,-57,-58]])
    expected = np.linalg.det(arr)
    test = matrix.get_determinant(arr)
    print(expected)
    print(test)
    assert expected == test
    
test_2x2_pos()
test_3x3_pos()
test_4x4_neg()
