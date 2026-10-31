# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue=[]
        a=[]
        s=[]
        queue.append(root)
        queue.append(None)
        while queue:
            curr=queue.pop(0)
            if curr is None:
                s.append(a)
                a=[]
                if len(queue)==0:
                    break
                else:
                    queue.append(None)
            else:
                a.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return s
        