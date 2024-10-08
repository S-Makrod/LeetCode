from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        sol = True

        def isBalancedHelper(root: Optional[TreeNode]) -> int:
            nonlocal sol
            if root is None or not sol:
                return 0

            r = isBalancedHelper(root.right)
            l = isBalancedHelper(root.left)

            sol = abs(r - l) <= 1 and sol

            return 1 + max(l, r)

        isBalancedHelper(root)
        return sol

