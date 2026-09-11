# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.l1 = []
        self.traverseTree(root, 0)

        return self.formatList()

    def traverseTree(self, curr, count):
        if curr:
            self.l1.append((curr.val, count))
            count += 1
        
            self.traverseTree(curr.left, count)
            self.traverseTree(curr.right, count)
        
        return 0
    
    def formatList(self):
        grouped = defaultdict(list)
        for val, index in self.l1:
            grouped[index].append(val)
        
        result = [grouped[k] for k in sorted(grouped.keys())]
        return result

