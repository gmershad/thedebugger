# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d = {}
        self.treeSum(root, d)
        mostFreq = 0
        if d:
            mostFreq = max(d[k] for k in d)
        
        return [k for k in d if d[k] == mostFreq]
    
    def treeSum(self, node, d):
        if not node:
            return 0
        
        l = self.treeSum(node.left, d)
        r = self.treeSum(node.right, d)
        v = node.val + l + r
        d[v] = d.get(v, 0) + 1
        return v
        
