"""
Script to write the test for the sum and substract functions
"""
import unittest
from Scripts.simple import sum_two_nums, sub_two_nums


class TestSimpleFunctions(unittest.TestCase):   #Importante todo los test han de empezar con la palabra test
    """
    Test simple functions sum & subtract
    """

    def test_sum(self):
        """
        Test the sum function
        """
        result = sum_two_nums(4,5)
        self.assertEqual(result,9) #AssertEqual viene de la funcion unittest.TestCase y lo que escribimos es que el resultaado ha de ser igual a 9.

    def test_sub(self):
        """
        Test the sub function
        """
        result = sub_two_nums(1,3)
        self.assertEqual(result, -2)        

if __name__ =="__main__":
    unittest.main()
