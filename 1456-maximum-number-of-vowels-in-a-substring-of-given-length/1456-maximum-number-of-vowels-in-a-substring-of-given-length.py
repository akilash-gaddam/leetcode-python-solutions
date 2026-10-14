class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l,r=0,0
        c=0
        m_c=0
        a=""
        while(r<len(s)):
            a+=s[r]
            if s[r] in "aeiou":
                c+=1
            if r-l+1 == k:
                if m_c < c:
                    m_c=c
                if s[l] in "aeiou":
                    c-=1
                l+=1
            r+=1
        return m_c




            

