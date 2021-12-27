class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in pairs and stack:
                if stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)
        
        if len(stack) == 0:
            return True
        
        return False
        