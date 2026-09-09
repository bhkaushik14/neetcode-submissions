# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        self.count = 0
        if not curr:
            return 0
        
        return self.traverseTree(curr, k)


    def traverseTree(self, curr, k):
        if curr and curr.left:
            result = self.traverseTree(curr.left, k)
            if result != 0:
                return result
        if curr:
            self.count += 1
            if self.count == k:
                return curr.val
        if curr and curr.right:
            result = self.traverseTree(curr.right, k)
            if result != 0:
                return result
        
        return 0
        

