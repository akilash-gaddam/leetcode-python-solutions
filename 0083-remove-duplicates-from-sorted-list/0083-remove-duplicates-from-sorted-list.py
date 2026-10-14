# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        self.curr=head
        while self.curr and self.curr.next:
            if self.curr.val == self.curr.next.val:
                self.curr.next=self.curr.next.next
            else:
                self.curr=self.curr.next
        return head
        
        