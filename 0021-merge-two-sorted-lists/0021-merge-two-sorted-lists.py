# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l=p=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                l.next=list1
                list1=list1.next
                l=l.next
            else:
                l.next=list2
                list2=list2.next
                l=l.next
        l.next = list1 if list1 else list2
        return p.next
                


        