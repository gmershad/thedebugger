class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        
        count = 0
        
        for c in s:
            if c == '(' and count > 0:
                res += c
            
            if c == '(':
                count += 1
            if c == ')' and count > 1:
                res += c
            
            if c == ')':
                count -= 1
            
        return res
