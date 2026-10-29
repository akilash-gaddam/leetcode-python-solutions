class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        h={}
        for i in s1.split():
            if i not in h :
                h[i] = 1
            else:
                h[i]+=1
        for i in s2.split():
            if i not in h :
                h[i] = 1
            else:
                h[i]+=1
        return [word for word,freq in h.items() if freq == 1]

        