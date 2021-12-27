# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        if head == None:
            return True
        
        if root == None:
            return False
        
        if self.dfs(head, root):
            return True
        
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    def dfs(self, head, root):
        if head == None:
            return True
        
        if root == None:
            return False
        
        if head.val == root.val:
            return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)
        
        return False
    
    
    
