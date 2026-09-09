# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        self.l1 = []
        if not curr:
            return 0
        
        self.traverseTree(curr)

        self.l1.sort()

        return self.l1[k - 1]

    def traverseTree(self, curr):
        if curr:
            self.l1.append(curr.val)

            self.traverseTree(curr.left)
            self.traverseTree(curr.right)

