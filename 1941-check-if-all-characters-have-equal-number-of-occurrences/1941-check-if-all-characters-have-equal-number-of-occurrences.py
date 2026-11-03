class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=d[i]
        for i,j in d.items():
            if j != c:
                return False
        return True

        