class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures) 
        stack = []
        res = [0] * n 

        for i in range(n): 
            today_temp = temperatures[i]

            while len(stack) > 0 : 
                top_index = stack[-1]
                top_temp = temperatures[top_index]
                if today_temp > top_temp : 
                    stack.pop()
                    res[top_index] = i - top_index
                else:
                    break 
            stack.append(i)
        return res
        