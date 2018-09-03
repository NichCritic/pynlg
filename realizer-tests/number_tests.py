'''
Created on 2013-03-06

@author: Nich
'''
import unittest
from pynlg.realizer import num_to_words

class TestNumber(unittest.TestCase):


    def setUp(self):
        pass
        
        
        

    def tearDown(self):
        pass


    def testOnes(self):
        self.assertEqual(num_to_words(1), "one")
        self.assertEqual(num_to_words(2), "two")
        self.assertEqual(num_to_words(3), "three")
        self.assertEqual(num_to_words(4), "four")
        self.assertEqual(num_to_words(5), "five")
        self.assertEqual(num_to_words(6), "six")
        self.assertEqual(num_to_words(7), "seven")
        self.assertEqual(num_to_words(8), "eight")
        self.assertEqual(num_to_words(9), "nine")

    def testTens(self):
        self.assertEqual(num_to_words(10), "ten")
        self.assertEqual(num_to_words(11), "eleven")
        self.assertEqual(num_to_words(12), "twelve")
        self.assertEqual(num_to_words(13), "thirteen")
        self.assertEqual(num_to_words(15), "fifteen")
        self.assertEqual(num_to_words(18), "eighteen")
        self.assertEqual(num_to_words(14), "fourteen")
        self.assertEqual(num_to_words(16), "sixteen")
        self.assertEqual(num_to_words(17), "seventeen")
        self.assertEqual(num_to_words(19), "nineteen")

    def testTwenties(self):
        self.assertEqual(num_to_words(20), "twenty")
        self.assertEqual(num_to_words(25), "twenty-five")



    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()