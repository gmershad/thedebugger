# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.result = set()
        self.dfs(root, 0)
        

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        if target in self.result:
            return True

        return False
        
    def dfs(self, root, val):
        if root == None:
            return
        
        self.result.add(val)
        
        if root.left:
            self.dfs(root.left, val * 2 + 1)
        
        if root.right:
            self.dfs(root.right, val * 2 + 2)
        
        
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
