# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
          if not root: 
           return []
          res = []
          queue = [root]
      
         
          while queue: 
            curr_length = len(queue)
            level = []
            for i in range(curr_length): 
              x = queue.pop(0)
              level.append(x.val)
              if x.left: 
                queue.append(x.left)
              if x.right: 
                queue.append(x.right)
            res.append(level)
       
          return res


