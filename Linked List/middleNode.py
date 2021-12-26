# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rabbit = head
        turtle = head
        while rabbit and rabbit.next:
            rabbit = rabbit.next.next
            turtle = turtle.next
            
        return turtle
            
