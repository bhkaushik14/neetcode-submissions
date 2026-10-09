# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.s = ""

        if root:
            self.recurseTree(root)

        return self.s

    def recurseTree(self, curr):
        if curr:
            self.s += str(curr.val) + " "
            self.recurseTree(curr.left)
            self.recurseTree(curr.right)
        else:
            self.s += "# "
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split()
        self.idx = 0
        return self.buildTree(vals)

    def buildTree(self, vals):
        if self.idx >= len(vals):
            return None

        val = vals[self.idx]
        self.idx += 1

        if val == "#":
            return None

        curr = TreeNode(int(val))

        curr.left = self.buildTree(vals)
        curr.right = self.buildTree(vals)

        return curr

        

