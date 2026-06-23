# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        out = []
        #preorder iteration to create
        def dfs(root):
            if not root:
                out.append('#') #we will use this for our nulls
                return
            out.append(str(root.val))
            dfs(root.left) 
            dfs(root.right)
        dfs(root)
        return ','.join(out)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = iter(data.split(','))
        def dfs():
            node = next(nodes)
            if node == '#':
                return None
            root = TreeNode(int(node))
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()


