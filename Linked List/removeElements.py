# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        node = head
        
        if node == None:
            return head

        while node.next != None:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        if head != None and head.val == val:
             head = head.next

        
        
        return head
