# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        inorder = []

        self.helpTraversal(curr, inorder)

        return inorder

    def helpTraversal(self, curr, inorder):
        if curr:
            self.helpTraversal(curr.left, inorder)
            inorder.append(curr.val)
            self.helpTraversal(curr.right, inorder)
        
            

    