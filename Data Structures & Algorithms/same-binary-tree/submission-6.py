# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.checkTrees(p, q)
    
    def checkTrees(self, curr_p, curr_q):
        if not curr_p and curr_q:
            return False
        
        if not curr_q and curr_p:
            return False

        if not curr_p and not curr_q:
            return True

        if curr_p.val != curr_q.val:
            return False
        
        return self.checkTrees(curr_p.left, curr_q.left) and self.checkTrees(curr_p.right, curr_q.right)
        