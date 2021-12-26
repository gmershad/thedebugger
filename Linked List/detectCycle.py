# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return
        
        slow = head.next
        fast = head.next.next
        
        while fast and fast.next and fast != slow:
            slow = slow.next
            fast = fast.next.next
            
        if fast is None or fast.next == None:
            return 
        
        while fast != head:
            head = head.next
            fast = fast.next
            
        return fast
