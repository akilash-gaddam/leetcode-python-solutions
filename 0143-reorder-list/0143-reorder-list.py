# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        stack=[]
        fast=head
        slow=head
        while (fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        curr=slow.next
        slow.next=None
        while(curr):
            stack.append(curr.val)
            curr=curr.next
        temp=head
        while stack:
            temp2 = temp.next
            temp.next=ListNode(stack.pop())
            temp=temp.next
            temp.next=temp2
            temp=temp.next
        
        