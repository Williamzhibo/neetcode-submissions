# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root: Optional[TreeNode], maximum: int, minimum: int) -> bool:
            if not root:
                return True
            
            if (maximum is not None and root.val >= maximum) or (minimum is not None and root.val <= minimum):
                return False

            return dfs(root.left, root.val, minimum) and dfs(root.right, maximum, root.val)
        return dfs(root, None, None)
