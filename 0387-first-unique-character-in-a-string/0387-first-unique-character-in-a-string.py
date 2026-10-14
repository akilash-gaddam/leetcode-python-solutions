class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash={}
        for i in s:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        for i in s:
            if hash[i] == 1 :
                return s.index(i)
        return -1