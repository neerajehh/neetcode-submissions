class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        columns = []
        boxes = []
        for i in range(9): 
            rows.append(set())
            columns.append(set())
            boxes.append(set())
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".": # skips non numbers 
                    continue
                index = (r//3) * 3 + (c//3) #index for the 9 squares 
                if val in rows[r] or val in columns[c] or val in boxes[index]: 
                    return False 
                rows[r].add(val)
                columns[c].add(val)
                boxes[index].add(val)
        return True
                    

