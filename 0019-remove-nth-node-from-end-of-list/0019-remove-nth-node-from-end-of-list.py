# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0,head)
        slow=dummy
        fast=dummy
        c=0
        if slow.next is None:
            return None
        while slow.next is not None:
            while fast.next is not None:
                fast=fast.next
                c+=1
            if c == n:
                slow.next = slow.next.next
                break
            else:
                slow = slow.next
                fast=slow
                c=0
        return dummy.next


            
        