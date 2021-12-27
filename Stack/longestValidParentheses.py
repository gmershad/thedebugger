class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        stack = []
        stack.append(-1)
        result = 0
        
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            else:
                if len(stack) > 0:
                    stack.pop()
                
                if len(stack) > 0:
                    result = max(result, (i - stack[len(stack) - 1]))
                else:
                    stack.append(i)
        
        return result
                    
                
                
