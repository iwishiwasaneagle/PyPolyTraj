from pypolytraj import *

import numpy as np
import unittest

class TestExceptions(unittest.TestCase):
    def test_invalidInput_quintic(self):
        valid_input = [[0,0],[1,1],[0,0],[0,0],[0,0],[0,0],1.0]

        for invalid_input in range(len(valid_input)):

            with self.assertRaises(TypeError):
                temp_valid_inp = np.copy(valid_input,dtype='object')
                temp_valid_inp[invalid_input] = "string"                
                QuinticPolynomialTrajectory(*temp_valid_inp)
            
            with self.assertRaises(TypeError):
                temp_valid_inp = np.copy(valid_input,dtype='object')
                temp_valid_inp[invalid_input] = [1,1,1]                
                QuinticPolynomialTrajectory(*temp_valid_inp)

if __name__ == '__main__':
    unittest.main()