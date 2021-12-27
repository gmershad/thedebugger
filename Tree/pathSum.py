# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        ret = []
        
        def findSum(root, path, partial):
            if not root.left and not root.right:
                if (partial+root.val) == targetSum:
                    ret.append(path+[root.val])
                return
            
            if root.left:
                findSum(root.left, path+[root.val], partial+root.val)
            if root.right:
                findSum(root.right, path+[root.val], partial+root.val)
        
        findSum(root, [], 0)
        return ret
                        
