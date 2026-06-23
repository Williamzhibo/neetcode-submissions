# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goods = 0
        def gN(root:TreeNode, greatest) -> int:
            if not root:
                return 0
            nonlocal goods
            out = greatest
            if root.val >= greatest:
                goods += 1
                out = root.val
            
            gN(root.left, out)
            gN(root.right, out)
        gN(root, float('-infinity'))
        return goods
            


