class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        v = []
        
        for i in ops:
            if i == '+':
                v.append(v[-1] + v[-2])
            elif i == 'D':
                v.append(v[-1] * 2)
            elif i == 'C':
                v.pop()
            else:
                v.append(int(i))
                
        return sum(v)
