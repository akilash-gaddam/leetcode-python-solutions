# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        return self.s(root.left,root.right)
    def s(self,p,q):
        if not p and not q:
            return True
        elif (not p and q) or (not q and p) or p.val != q.val :
            return False
        return self.s(p.left,q.right) and self.s(p.right,q.left) and p.val == q.val

        