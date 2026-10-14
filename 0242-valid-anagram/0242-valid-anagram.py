class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        for i in t:
            s=s.replace(i,'',1)
        if len(s)==0:
            return True
        return False