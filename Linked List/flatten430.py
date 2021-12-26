"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        current = head
        
        while current is not None:
            if current.child is not None:
                self.merge(current)
            
            current = current.next
        
        return head
        
    def merge(self, current):
        child = current.child
        
        # traverse child list until we get the last node
        while child.next is not None:
            child = child.next
        
        # child is now pointing at the last node of the child list
        # we need to connect child.next to current.next, if there is any
        if current.next is not None:
            child.next = current.next
            current.next.prev = child
        
        # now, we have to connect current to the child list
        # child is currently pointing at the last node of the child list, 
        # so we need to use pointer (current.child) to get to the first node of the child list
        current.next = current.child
        current.child.prev = current
        
        # at the end remove self.child pointer
        current.child = None
        
