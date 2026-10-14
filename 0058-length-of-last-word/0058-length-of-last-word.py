class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s[::-1]
        c=0
        for i in s:
            if i == " " and c == 0:
                continue
            elif i == " " and c!=0:
                break
            c+=1
        return c