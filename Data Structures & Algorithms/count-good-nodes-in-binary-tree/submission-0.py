# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        value = root.val
        return self.recurseNodes(root, value)   

    def recurseNodes(self, curr, value):
        if not curr:
            return 0

        if value < curr.val:
            value = curr.val
        return self.recurseNodes(curr.left, value) + self.recurseNodes(curr.right, value) + (1 if value is curr.val else 0)
