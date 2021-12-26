# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        ptr1 = head
        while k > 1:
            ptr1 = ptr1.next
            k -= 1
        
        ptr1Next = ptr1.next
        ptr2 = head
        while ptr1Next:
            ptr1Next = ptr1Next.next
            ptr2 = ptr2.next
        
        ptr1.val, ptr2.val = ptr2.val, ptr1.val
        return head
            
