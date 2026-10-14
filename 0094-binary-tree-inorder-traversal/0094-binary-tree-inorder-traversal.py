# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        r=[]
        def inorder(curr,r):
            if not curr:
                return
            
            inorder(curr.left,r)
            r.append(curr.val)
            inorder(curr.right,r)
        inorder(root,r)
        return r