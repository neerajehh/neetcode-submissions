class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        length = 0 
        for i in range(len(s)): 
            left = i
            right = i
            while left >= 0 and right<len(s) and s[left] == s[right]:  #Odd Palindromes 
                if right-left + 1 > length : 
                    length = right-left + 1 
                    res = s[left:right+1]
                left = left - 1 
                right = right + 1 
            left = i 
            right = i+1
            while left>=0 and right<len(s) and s[left] == s[right]: 
                if right - left + 1  + 1 > length: 
                    length = right-left+1
                    res = s[left:right+1]
                left = left-1
                right = right+1
        return res 


        