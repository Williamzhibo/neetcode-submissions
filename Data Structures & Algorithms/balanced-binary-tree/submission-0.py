# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def helper(root: Optional[TreeNode]):

            if not root:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            if left == -1 or right == -1:
                return -1

            res = left - right
            if abs(res) > 1:
                return -1
            return 1 + max(left, right)
        if helper(root) == -1:
            return False
        else:
            return True


