# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traverse(root, [])

    def traverse(self, curr, postorder):
        if curr:
            self.traverse(curr.left, postorder)
            self.traverse(curr.right, postorder)
            postorder.append(curr.val)
        
        return postorder