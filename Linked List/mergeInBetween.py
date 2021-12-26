# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        head = list1
        
        for _ in range(a-1):
            head = head.next
            
        curr = head.next
        
        for _ in range(b-a):
            curr = curr.next
        
        head.next = list2
        while head.next:
            head = head.next
        
        if curr.next:
            head.next = curr.next
        
        return list1
            
        
        
