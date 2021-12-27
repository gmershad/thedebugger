# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []

        def helper(root, temp):
            if not root: 
                return None
            
            if not root.left and not root.right: 
                res.append(temp + str(root.val))
                
            helper(root.left, temp + (str(root.val) + "->"))
            helper(root.right, temp + (str(root.val) + "->"))

        helper(root, "")
        return res
