# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
            
        i = 0
        s = 0
        while len(stack):
            s += stack.pop()*2**i
            i += 1
        return s
        
