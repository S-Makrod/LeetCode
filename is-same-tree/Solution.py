from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q is None and p is None:
            return True
        if q is not None and p is None:
            return False
        if q is None and p is not None:
            return False

        return p.val == q.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
