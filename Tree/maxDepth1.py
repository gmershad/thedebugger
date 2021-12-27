"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        
        maximum = 0
        for child in root.children:
            maximum = max(maximum, self.maxDepth(child))
            
        return (1 + maximum)
        
