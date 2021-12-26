# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        if head.next == None:
            return head
        
        mid = self.findMid(head)
        head2 = mid.next
        mid.next = None
        newHead1 = self.sortList(head)
        newHead2 = self.sortList(head2)
        
        finalHead = self.merge(newHead1, newHead2)
        
        return finalHead
    
    def findMid(self, head):
        slow = head
        fast = head.next
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def merge(self, head1, head2):
        merged = ListNode(-1)
        temp = merged
        
        while head1 != None and head2 != None:
            if (head1.val < head2.val):
                temp.next = head1
                head1 = head1.next
            else:
                temp.next = head2
                head2 = head2.next
            
            temp = temp.next
            
        while (head1 != None):
            temp.next = head1
            head1 = head1.next
            temp = temp.next
            
        while (head2 != None):
            temp.next = head2
            head2 = head2.next
            temp = temp.next
            
        return merged.next
    
    
        
        
        
