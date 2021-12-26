# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sorted = None
        current = head
        
        while current != None:
            next = current.next
            sorted = self.sortedInsert(sorted, current)
            current = next
        
        head = sorted
        return head
    
    def sortedInsert(self, temp, new_node):
        current = None
        
        if temp == None or temp.val >= new_node.val:
            new_node.next = temp
            temp = new_node
        else:
            current = temp
            while current.next != None and current.next.val < new_node.val:
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
        
        return temp
            
