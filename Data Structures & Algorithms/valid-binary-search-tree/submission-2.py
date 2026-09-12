# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        curr = root
        if not curr:
            return True

        return self.checkTree(curr, -1 * float("infinity"), float("infinity"))

    def checkTree(self, curr, lowerBound, upperBound) -> bool:
        if not curr:
            return True
        if lowerBound < curr.val and curr.val < upperBound:
            return self.checkTree(curr.left, lowerBound, curr.val) and self.checkTree(curr.right, curr.val, upperBound)
        
        return False