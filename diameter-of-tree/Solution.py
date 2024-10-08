from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        sol = 0

        def diameterOfBinaryTreeHelper(root: Optional[TreeNode]) -> int:
            nonlocal sol
            if root is None:
                return 0

            r = diameterOfBinaryTreeHelper(root.right)
            l = diameterOfBinaryTreeHelper(root.left)
            sol = max(sol, r + l)

            return 1 + max(r, l)

        diameterOfBinaryTreeHelper(root)
        return sol
