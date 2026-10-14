class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        l=""
        for i in s:
            if i.isalnum():
                l=l+i
        if l == "":
            return True
        elif l!=l[::-1]:
            return False
        return True