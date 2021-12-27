# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = [root.val]
        level = [root]
        
        while level:
            new_level = []
            level_sum = 0.0
            
            for node in level:
                if node.left:
                    new_level.append(node.left)
                    level_sum += node.left.val
                if node.right:
                    new_level.append(node.right)
                    level_sum += node.right.val
                    
            if new_level:
                res.append(level_sum / len(new_level))
            level = new_level
            
        return res
