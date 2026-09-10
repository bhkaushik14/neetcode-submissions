from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        self.l1 = [] # Stores pairs of (val, level)
        self.traverseTree(root, 0)
        return self.formatList()

    def traverseTree(self, curr, count):
        if curr:
            self.l1.append((curr.val, count))
            # Keep count unchanged for both children since they are on the same next level
            self.traverseTree(curr.left, count + 1)
            self.traverseTree(curr.right, count + 1)

    def formatList(self):
        # 1. Group the nodes by their level using a dictionary
        level_map = {}
        for val, level in self.l1:
            if level not in level_map:
                level_map[level] = []
            level_map[level].append(val)
            
        # 2. Reconstruct into a list of lists ordered by level
        new_l1 = []
        for level in range(len(level_map)):
            new_l1.append(level_map[level])
            
        return new_l1
