# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, res, 0)
        return res

    def dfs(self, curr, res, depth):
        if not curr:
            return
        
        if depth == len(res):
            res.append(curr.val)
        
        self.dfs(curr.right, res, depth+1)
        self.dfs(curr.left, res, depth+1)
        
        