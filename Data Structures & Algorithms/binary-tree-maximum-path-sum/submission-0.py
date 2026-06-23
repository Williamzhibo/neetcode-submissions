# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum = root.val
        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0
            nonlocal maximum
 
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            combined = left + right + root.val
            maximum = max(maximum, combined)
                        
            return root.val + max(left, right)
        dfs(root)
        return maximum

