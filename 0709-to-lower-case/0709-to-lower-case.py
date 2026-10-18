class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=""
        for i in s:
            if 65<= ord(i) <= 90:
                a += chr(ord(i)+32)
            else:
                a += i
        return a

        