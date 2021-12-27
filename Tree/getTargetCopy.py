# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        self.ans = 0
        self.inOrder(original, cloned, target)
        return self.ans
        
    
    def inOrder(self, original, cloned, target):
        if original:
            self.inOrder(original.left, cloned.left, target)
            if original is target:
                self.ans = cloned
            
            self.inOrder(original.right, cloned.right, target)
        
