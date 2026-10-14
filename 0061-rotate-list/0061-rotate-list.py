# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or head.next is None:
            return head
        if k==0:
            return head
        dummy=ListNode(0,head)
        temp=dummy.next
        arr=[]
        while temp is not None:
            arr.append(temp)
            temp=temp.next
        n=len(arr)
        k=k%n
        arr=arr[n-k:]+arr[:n-k]
        for i in range(n-1):
            arr[i].next=arr[i+1]
        arr[-1].next=None
        return arr[0]     

            
        