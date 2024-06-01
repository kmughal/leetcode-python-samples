import unittest
from main import *
class LeetCodeTests(unittest.TestCase):
    
    
    def test_problem_1(self):
        target = 9
        nums = [2,7,11,15]
        actual = problem1(nums, target)
        self.assertEqual([0,1], actual)
        
    def test_isPalindrome(self):
        self.assertTrue(isPalindrome(121))
        self.assertFalse(isPalindrome(123))
        
    def test_roman_int(self):
        self.assertEqual(1994, roman_int('MCMXCIV'))
        self.assertEqual(4, roman_int('IV'))
        
    def test_longestCommonPrefix(self):
        self.assertEqual('fl', longestCommonPrefix(['flower','flow','flight']))
        self.assertEqual('', longestCommonPrefix(['dog','racecar','car']))
        self.assertEqual('a', longestCommonPrefix(['a']))
        self.assertEqual('', longestCommonPrefix(['']))
    
    def test_is_valid_brackets(self):
        self.assertFalse(is_valid_brackets("[([]])"))
        self.assertTrue(is_valid_brackets("[]"))
        self.assertTrue(is_valid_brackets("[](){}"))
        self.assertFalse(is_valid_brackets("[(])"))
        self.assertTrue(is_valid_brackets("()"))
        self.assertTrue(is_valid_brackets("()[]{}"))
        self.assertFalse(is_valid_brackets("(]"))
        self.assertFalse(is_valid_brackets("([)]"))
        self.assertTrue(is_valid_brackets("{[]}"))
        
        
    def test_removeDuplicates(self):
        self.assertEqual(2, removeDuplicates([1,1,2]))
        self.assertEqual(5, removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
        self.assertEqual(1, removeDuplicates([1]))
        self.assertEqual(0, removeDuplicates([]))
if __name__ == '__main__':
    unittest.main()