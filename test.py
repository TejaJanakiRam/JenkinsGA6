#!/usr/bin/python3

import unittest

from multi import multi

class TestSum(unittest.TestCase):
    def test1(self):
        """
        Test case to multiply two numbers
        """
        
        result = multi(20,30)
        self.assertEqual(result, 400)
    def test2(self):
        """
        Test case to multiply two numbers
        """
        
        result = multi(20,30)
        self.assertEqual(result, 300)
    def test3(self):
        """
        Test case to muktiply two numbers
        """
        
        result = multi(20,30)
        self.assertEqual(result, 200)
    def test4(self):
        """
        Test case to multiply two numbers
        """
        
        result = multi(20,30)
        self.assertEqual(result, 600)
    def test5(self):
        """
        Test case to multiply two numbers
        """
        
        result = multi(20,40)
        self.assertEqual(result, 800)
if __name__ == '__main__':
    unittest.main()
