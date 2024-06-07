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
        
    def test_longestPalindrome(self):
        self.assertEqual('bab', longestPalindrome('babad'))
        self.assertEqual('bb', longestPalindrome('cbbd'))
        self.assertEqual('a', longestPalindrome('a'))
        self.assertEqual('a', longestPalindrome('ac'))
        self.assertEqual('a', longestPalindrome('abcda'))
        self.assertEqual('aa', longestPalindrome('aacdefcaa'))
        
        
    def test_findMedianSortedArrays(self):
        self.assertEqual(2.0, findMedianSortedArrays([1,3],[2]))
        self.assertEqual(2.5, findMedianSortedArrays([1,2],[3,4]))
        self.assertEqual(0.0, findMedianSortedArrays([0,0],[0,0]))
        self.assertEqual(1.0, findMedianSortedArrays([],[1]))
        self.assertEqual(2.0, findMedianSortedArrays([2],[]))
        self.assertEqual(1.0, findMedianSortedArrays([1,1],[1,2]))

    def test_removeElement(self):
        self.assertEqual(2, removeElement([3,2,2,3],3))
        self.assertEqual(5, removeElement([0,1,2,2,3,0,4,2],2))
        self.assertEqual(0, removeElement([],0))
        self.assertEqual(0, removeElement([1],1))
        self.assertEqual(1, removeElement([1],2))
        
        
    def test_strStr(self):
        self.assertEqual(2, strStr('hello','ll'))
        self.assertEqual(-1, strStr('aaaaa','bba'))
        self.assertEqual(0, strStr('',''))
        self.assertEqual(-1, strStr('mississippi','issipi'))
        self.assertEqual(4, strStr('mississippi','issip'))
        
    def test_searchInsert(self):
        self.assertEqual(2, searchInsert([1,3,5,6],5))
        self.assertEqual(1, searchInsert([1,3,5,6],2))
        self.assertEqual(4, searchInsert([1,3,5,6],7))
        self.assertEqual(0, searchInsert([1,3,5,6],0))
        self.assertEqual(0, searchInsert([1],0))
        self.assertEqual(1, searchInsert([1],2))
if __name__ == '__main__':
    unittest.main()