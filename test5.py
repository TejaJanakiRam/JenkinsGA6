#!/usr/bin/python3

import unittest

from multi import multi

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        
        result = multi(10,30)
        self.assertEqual(result, 300)

if __name__ == '__main__':
    unittest.main()