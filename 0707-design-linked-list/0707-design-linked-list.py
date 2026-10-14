class node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        # Index must be strictly less than the total size
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = node(val)
        if not self.head:
            self.head = new_node
            self.size += 1
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return

        new_node = node(val)
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
            
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        
        # If deleting the first element, move the head pointer forward
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
            
        curr = self.head
        # CRITICAL: Stop exactly at index - 1 (the node BEFORE deletion point)
        for _ in range(index - 1):
            curr = curr.next
            
        curr.next = curr.next.next
        self.size -= 1