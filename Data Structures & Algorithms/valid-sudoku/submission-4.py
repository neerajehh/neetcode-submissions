class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = []
        column = []
        box = []
        for i in range(9): 
            row.append(set())
            column.append(set())
            box.append(set())
        for r in range(9): 
            for c in range(9):
                val = board[r][c]
                if val == ".": 
                    continue
                a = ((r//3) * 3) + c//3
                if val in row[r] or val in column[c] or val in box[a]: 
                    return False
                row[r].add(val)
                column[c].add(val)
                box[a].add(val)
        return True  

                 
        
        