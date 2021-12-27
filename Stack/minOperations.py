class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        Operations = ['./', '../']
        stack = []
        
        for op in logs:
            if op not in Operations:
                stack.append(op)
            elif op == '../' and len(stack) > 0:
                stack.pop()
                
        
        return len(stack)
