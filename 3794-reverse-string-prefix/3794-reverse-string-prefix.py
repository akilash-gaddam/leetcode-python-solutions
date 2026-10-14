class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 1 or k == 0:
            return s
        return s[:k][::-1] + s[k:]

        