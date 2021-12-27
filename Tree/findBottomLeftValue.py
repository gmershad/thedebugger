# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [root.val, 0]
        self.search(root, res, 0)
        return res[0]
    
    def search(self, node, res, curDepth):
        if node:
            if curDepth > res[1]:
                res[0], res[1] = node.val, curDepth
            
            self.search(node.left, res, curDepth+1)
            self.search(node.right, res, curDepth+1)
