class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first binary search to find the correct row
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0 
        bot = rows - 1 
        while top<=bot: 
            row = (top+bot) // 2 
            if target>matrix[row][cols-1]: 
                top = row + 1 
            elif matrix[row][0]>target: 
                bot = row - 1 
            else:
                 break 
        if not top<=bot:
         return False
        l = 0 
        r = cols - 1 
        while l<=r:
            mid = (l+r) // 2 
            if target<matrix[row][mid]:
                r = mid - 1
            elif target>matrix[row][mid]: 
                 l = mid+1
            else:
                 return True 
        return False 
