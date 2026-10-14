# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        r=[]
        def postorder(curr,r):
            if curr is None:
                return
            postorder(curr.left,r)
            postorder(curr.right,r)
            r.append(curr.val)
        postorder(root,r)

        return r
        