class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for x in s : 
            if x.isalnum(): 
                new_str+=x.lower()
        return new_str == new_str[::-1]
        