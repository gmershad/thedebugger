# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        slow = head
        stack = []
        
        while slow:
            stack.append(slow.val)
            slow = slow.next
        
        while head:
            i = stack.pop()
            if i != head.val:
                return False
            
            head = head.next
        
        return True
                
        
