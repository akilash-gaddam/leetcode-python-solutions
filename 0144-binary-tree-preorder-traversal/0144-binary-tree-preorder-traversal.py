# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r=[]
        def preorder(curr,r):
            if not curr:
                return
            r.append(curr.val)
            preorder(curr.left,r)
            preorder(curr.right,r)
        preorder(root,r)

        return r