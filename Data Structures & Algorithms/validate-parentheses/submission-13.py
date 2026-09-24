class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s_map = { "]":"[" , ")":"(" , "}" : "{"}
        for c in s : 
            if c in s_map: 
                if stack and stack[-1] == s_map[c]: 
                    stack.pop()
                else:
                     return False
            else:
                stack.append(c)
        return len(stack) == 0 
        