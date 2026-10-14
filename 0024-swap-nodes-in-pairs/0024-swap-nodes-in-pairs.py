# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0,head)
        first=head
        prev=dummy
        while first is not None and first.next is not None:
            second=first.next
            first.next=first.next.next
            second.next = first
            if prev is not None:
                prev.next=second
            prev=first
            first = first.next
        return dummy.next

            
        