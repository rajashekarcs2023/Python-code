from typing import Optional 
class TreeNode:  # {{ edit_1 }}
    def __init__(self, val=0, left=None, right=None):  # {{ edit_2 }}
        self.val = val
        self.left = left
        self.right = right
class Solution():
    def invertBinaryTree(self,root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)

        return root