class Solution(object):
    def zero(self):
        return 0
    
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_table = defaultdict(self.zero)
        
        for i in s:
            hash_table[i] += 1
            
        for i in range(len(s)):
            if hash_table[s[i]] == 1:
                return i
            
        return -1
