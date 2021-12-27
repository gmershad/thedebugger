class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        output = []
        for i in range(1, target[-1]+1):
            if i in target:
                output.append("Push")
            else:
                output.append("Push")
                output.append("Pop")
            
        return output
        
