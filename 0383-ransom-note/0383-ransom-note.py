class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        l=len(magazine)
        for i in ransomNote:
            if i in magazine:
                k=magazine.index(i)
                magazine=magazine[:k]+magazine[k+1:]

        if l == len(magazine)+len(ransomNote):
            return True
        return False

