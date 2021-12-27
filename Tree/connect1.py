"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        
        par, child_root = root, Node()
        child = child_root
        
        while child and par:
            if par.left:
                child.next = par.left
                child = child.next
            if par.right:
                child.next = par.right
                child = child.next
            par = par.next            
            
        self.connect(child_root.next)
        return root
        
        
        
