class Solution:
 def isValidSudoku(self, board: List[List[str]]) -> bool:
    rows = [set() for x in range(9)]
    columns =  [ set() for x in range(9)]
    box = [ set() for x in range(9)]

    for row in range(9):
     for column in range(9):
      num = board[row][column] 
      if num == '.': 
       continue 
      box_row = row // 3 
      box_column = column//3 
      box_index = box_row * 3 + box_column 

      if num in rows[row]:
       return False 
      if num in columns[column]:
       return False 
      if num in box[box_index]: 
        return False 

      rows[row].add(num)
      columns[column].add(num)
      box[box_index].add(num)
 
    return True 

