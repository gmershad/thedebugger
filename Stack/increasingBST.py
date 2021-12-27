# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inOrder(node):
            if node:
                inOrder(node.left)
                node.left = None
                self.curr.right = node
                self.curr = node
                inOrder(node.right)
            
        ans = self.curr = TreeNode(None)
        inOrder(root)
        return ans.right
        
