# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        l = 0
        r = len(nums) - 1
        
        def build(nums, l, r):
            if l > r:
                return None
            
            m = (l + r + 1) // 2
            
            root = TreeNode(nums[m])
            root.left = build(nums, l, m-1)
            root.right = build(nums, m+1, r)
            
            return root
        
        return build(nums, l, r)
        
      
        
