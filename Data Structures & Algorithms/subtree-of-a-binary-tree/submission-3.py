# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        curr = root
        if not subRoot:
            return False
        
        if not curr:
            return False
        
        if curr.val == subRoot.val:
            if self.checkTree(curr, subRoot):
                return True

        return self.isSubtree(curr.left, subRoot) or self.isSubtree(curr.right, subRoot)


    def checkTree(self, curr, sub_curr):
        if not curr and not sub_curr:
            return True
        
        if not curr:
            return False
        
        if not sub_curr:
            return False

        if curr.val == sub_curr.val:
            return self.checkTree(curr.left, sub_curr.left) and self.checkTree(curr.right, sub_curr.right)
        
        return False