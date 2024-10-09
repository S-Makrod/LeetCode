from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def levelOrderHelper(root: Optional[TreeNode]) -> List[List[int]]:
            if root is None:
                return []

            r = levelOrderHelper(root.right)
            l = levelOrderHelper(root.left)

            merge = []

            for i in range(max(len(r), len(l))):
                if i < len(r) and i < len(l):
                    merge.append(l[i] + r[i])
                elif i < len(r):
                    merge.append(r[i])
                else:
                    merge.append(l[i])

            curr = []
            if root.left:
                curr.append(root.left.val)
            if root.right:
                curr.append(root.right.val)

            return [] if not curr else [curr] + merge

        return [] if not root else [[root.val]] + levelOrderHelper(root)