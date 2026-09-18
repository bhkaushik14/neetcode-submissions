# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}

        for index, value in enumerate(inorder):
            inorder_map[value] = index

        self.preorder_index = 0

        def build(left, right):
            if left > right:
                return None

            root_value = preorder[self.preorder_index]
            self.preorder_index += 1

            root = TreeNode(root_value)

            root_index = inorder_map[root_value]

            root.left = build(left, root_index - 1)
            root.right = build(root_index + 1, right)

            return root

        return build(0, len(inorder) - 1)
