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
                value = board[r][c]
                if value == ".": 
                    continue 
                index = ((r//3) * 3 ) + (c//3)
                if value not in rows[r] and value not in columns[c] and value not in boxes[index]:
                    rows[r].add(value)
                    columns[c].add(value)
                    boxes[index].add(value)
                else:
                     
                     return False
        return True
                
        