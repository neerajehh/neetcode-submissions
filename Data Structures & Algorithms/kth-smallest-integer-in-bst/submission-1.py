# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
       result = [0]
       count = [0] 
       def level(node):
        if not node: 
            return
        level(node.left)
        count[0] = count[0] + 1 
        if count[0] == k :
            result[0] = node.val
            return 
        level(node.right)
       level(root)
       return result[0] 

        