# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out: List[List[int]] = []

        def levelOrder(root:Optional[TreeNode], depth: int):
            nonlocal out 

            if not root:
                return

            if depth == len(out):
                out.append([])
        
            out[depth].append(root.val)
            levelOrder(root.left, depth+1)
            levelOrder(root.right, depth+1)

        levelOrder(root, 0)

        return out