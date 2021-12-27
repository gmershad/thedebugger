"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        self.post(root, res)
        return res
        
    def post(self, node, res):
        if node:
            for child in node.children:
                self.post(child, res)
                
            res.append(node.val)
                
