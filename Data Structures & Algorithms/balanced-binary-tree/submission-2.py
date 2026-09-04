# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkBalance(root)

    def treeHeight(self, curr):
        if not curr:
            return 0

        return 1 + max(self.treeHeight(curr.left), self.treeHeight(curr.right))
    
    def checkBalance(self, curr):
        if not curr:
            return True
        
        left = self.treeHeight(curr.left)
        right = self.treeHeight(curr.right)

        if abs(left - right) > 1:
            return False

        return self.checkBalance(curr.left) and self.checkBalance(curr.right)