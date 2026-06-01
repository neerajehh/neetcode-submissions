class Solution:
  def isPalindrome(self, s: str) -> bool:
    left = 0 
    right = len(s)-1 
    while left<right : 
        while left<right and  not isAlumn(s[left]):
            left = left+1

        while left<right and not isAlumn(s[right]):
            right = right-1 

        if s[left].lower() != s[right].lower():
            return False 
        
        left = left+1 
        right = right-1


    return True 
def isAlumn(c):
    
        return ( 'A'<=c<='Z' or 'a'<=c<='z' or '0'<=c<='9')
    