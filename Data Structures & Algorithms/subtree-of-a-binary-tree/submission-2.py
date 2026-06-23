# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            left, right = sameTree(p.left, q.left), sameTree(p.right, q.right)
            return p.val == q.val and left and right
        
        def dfs(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root:
                return False
            
            if root.val == subRoot.val and sameTree(root, subRoot):
                return True
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        return dfs(root, subRoot)