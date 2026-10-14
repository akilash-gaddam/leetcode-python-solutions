# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        temp=head
        l=[]
        while temp:
            if temp.val != val:
                l.append(temp)
                temp=temp.next
            else:
                temp=temp.next
        n=len(l)
        if n == 0:
            return None
        for i in range(n-1):
            l[i].next=l[i+1]
        l[n-1].next=None
        return l[0]

            


        