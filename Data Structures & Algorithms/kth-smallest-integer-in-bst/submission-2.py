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
        self.count = 0
        if not curr:
            return 0
        
        self.traverseTree(curr)

        return self.l1[k - 1]

    def traverseTree(self, curr):
        if curr and curr.left:
            self.traverseTree(curr.left)
        if curr:
            self.l1.append(curr.val)
            self.count += 1
            if self.count == k:
                return
        if curr and curr.right:
            self.traverseTree(curr.right)
        

