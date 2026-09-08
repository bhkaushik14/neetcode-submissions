# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        self.findHeight(root)
        return self.maxDiameter

    def findHeight(self, curr):
        if not curr:
            return 0

        left = self.findHeight(curr.left)
        right = self.findHeight(curr.right)

        self.maxDiameter = max(self.maxDiameter, left + right)

        return 1 + max(left, right)