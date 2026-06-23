# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []
        def dfs(root: Optional[TreeNode]):
            if not root:
                return 
            nonlocal lst
            lst.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        lst.sort()

        return lst[k-1]
