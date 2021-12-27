# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(n):
            if n:
                if smallest < n.val < self.second:
                    self.second = n.val
                elif smallest == n.val: # bcuz of the property of this special bt 
                    inorder(n.left)
                    inorder(n.right)
                    
        smallest = root.val
        self.second = float('inf')
        inorder(root)
        return self.second if self.second != float('inf') else -1
