# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    # Needs to be O(n) or O(nLogn)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        curr = root
        self.best = -1* math.inf

        total = self.totalSum(curr)

        return self.best

    def totalSum(self, curr):
        if not curr:
            return 0
            
        left = self.totalSum(curr.left)
        right = self.totalSum(curr.right)

        if left < 0:
            left = 0
        if right < 0:
            right = 0

        if self.best < left + curr.val + right:
            self.best = curr.val + right + left
        return curr.val + max(left, right)
    