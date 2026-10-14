# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp1=l1
        temp2=l2
        s=ListNode(0)
        dummy=s
        a=0
        b=0
        mult=1
        while temp1:
            a+=temp1.val*mult
            mult*=10
            temp1=temp1.next
        mult=1
        while temp2:
            b+=temp2.val*mult
            mult*=10
            temp2=temp2.next
        sums=a+b
        if  sums==0:
            return ListNode(0)
        while sums>0:
            rem=sums%10
            sums=sums//10
            dummy.next=ListNode(rem)
            dummy=dummy.next
        return s.next
        



            
        