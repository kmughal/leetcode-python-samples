from typing import List, Optional


def problem1(arr,target):
    for i,v in enumerate(arr):
        for j,w in enumerate(arr):
            if v+w == target:
                return [i,j]
nums = [2,7,11,15]
target = 9
# print(problem1(nums,target))

def isPalindrome(x:int)-> str:
    to_str = str(x)
    return to_str == to_str[::-1]

 

def roman_int(s:str)->int:
    keys = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    r = 0

    for i,v in enumerate(s):
        roman_special_rules = v in keys and i+1 < len(s) and s[i+1] in keys
        if not roman_special_rules:
            r += keys[v]
            continue
        n = keys[s[i+1]]
        g = keys[v]
        r = r - g if g<n else r + g
    return r
        
        
        

def longestCommonPrefix(strs: List[str]) -> str:
    common = ''
    for v in strs[0]:
        common += v
        for i in range(1,len(strs)):
            if strs[i].startswith(common) == False:
               return common[:-1]
    return common


def is_valid_brackets(s):
    stack = []
    bracket_map = {"(": ")", "[": "]", "{": "}"}

    for char in s:
        if char in bracket_map:
            stack.append(char)
        elif not stack or bracket_map[stack.pop()] != char:
            return False

    return not stack



def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1
    
def longestPalindrome(s: str) -> str:
    if len(s) == 1:
        return s

    n = len(s)
    longest_len = 1
    start = 0
    dp = [[False] * n for _ in range(n)]

    for j in range(1, n):
        for i in range(j):
            if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if j - i + 1 > longest_len:
                    longest_len = j - i + 1
                    start = i

    return s[start:start + longest_len]

s1 = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
        


def findMedianSortedArrays(nums1,nums2):
    c = sorted(nums1 + nums2)
    middle = len(c) // 2
    ans = ((c[middle] + c[middle-1]) / 2) if len(c) % 2 == 0 else (c[middle])
    return ans


 
def removeElement(nums: List[int], val: int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i


def strStr(haystack: str, needle: str) -> int:
    try:
        return haystack.index(needle)
    except:
        return -1
    
    
def searchInsert(nums:List[int],tt:int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] < tt:
            i += 1
    return i

def lengthOfLastWord( s: str) -> int:
    c = s.split(' ')
    l = filter(lambda x: x != '', c)
    gg = list(l)
    return len(gg[-1]) if len(gg) > 0 else 0

def plusOne(input: List[int]) -> List[int]:
    d = input[::-1]
    carry = 1
    for i in range(len(d)):
        d[i] += carry
        carry = d[i] // 10
        d[i] %= 10
    if carry:
        d.append(1)
    return d[::-1]

def addBinary(num1: str, num2: str) -> str:
    l = max(len(num1), len(num2))
    p = 0
    r = ''
    num1 = num1.zfill(l)
    num2 = num2.zfill(l)
    
    for i in range(l - 1, -1, -1):
        a = int(num1[i])
        b = int(num2[i])
        
        t = a + b + p
        q = t % 2  
        p = t // 2  
        r = str(q) + r  

    if p == 1:
        r = f'1{r}'

    return r


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class AddLinkLists:
    def append(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return ListNode(val)
        
        current = head 
        while current.next:
            current = current.next 
        current.next = ListNode(val)
        return head
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x1 = l1
        x2 = l2
        r:Optional[ListNode] = None
        carry = 0
        print(f"Initial values: {x1}, {x2}")
        while x1 or x2:
            a = x1.val if x1 else 0
            b = x2.val if x2 else 0
            total = a + b + carry
            if total < 10:
                r = self.append(r, total)
                carry = 0
            else:
                r = self.append(r, total % 10)
                carry = total // 10
            
            x1 = x1.next if x1 else 0
            x2 = x2.next if x2 else 0
        if carry > 0:
            r = self.append(r, carry)
        return r