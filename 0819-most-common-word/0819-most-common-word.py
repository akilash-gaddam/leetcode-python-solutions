class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        d={}
        for i in paragraph:
            if i in "!?',;.":
                paragraph=paragraph.replace(i," ")
        paragraph=paragraph.lower().split()
        for i in paragraph:
            if i in d:
                d[i]+=1
            elif i not in d:
                d[i]=1
        m=""
        maxi=0
        for i,j in d.items() :
            if j > maxi and i not in banned :
                maxi=j
                m=i
        return m

        