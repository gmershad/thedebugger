"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return head
        
        d = {}
        curr = head
        while curr != None:
            d[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        
        while curr != None:
            if curr.next == None:
                d[curr].next = None
            else:
                d[curr].next = d[curr.next]
            
            if curr.random == None:
                d[curr].random = None
            else:
                d[curr].random = d[curr.random]
            
            curr = curr.next
        
        return d[head]
