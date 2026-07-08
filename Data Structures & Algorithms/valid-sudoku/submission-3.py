class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
     rows = []
     columns = []
     box = []
     for r in range(9): 
        rows.append(set())
        columns.append(set())
        box.append(set())
     for r in range(9):
        for c in range(9): 
            val = board[r][c]
            if val == ".":
                continue
            box_index = ((r//3) * 3) + (c//3)
            if val in rows[r] or val in columns[c] or val in box[box_index]:
                return False 
            rows[r].add(val)
            columns[c].add(val)
            box[box_index].add(val)
     return True

