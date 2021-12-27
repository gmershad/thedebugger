# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = 0
        
        def helper(root,nums):
            if not root.left and not root.right:
                nums += str(root.val)
                self.total += int(nums,2)
                return    
            
            nums += str(root.val)
            if root.left:
                helper(root.left,nums)
            
            if root.right:
                helper(root.right,nums)
                
        helper(root, "")
        return self.total
