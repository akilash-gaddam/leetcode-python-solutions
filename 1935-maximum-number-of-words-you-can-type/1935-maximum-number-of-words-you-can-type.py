class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        s=set(brokenLetters)
        text=text.split(" ")
        c=0
        for i in text:
            for j in i:
                if j in s:
                    c+=1
                    break
        return len(text)-c


        


        