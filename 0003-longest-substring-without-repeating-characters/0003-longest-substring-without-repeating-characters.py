class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={}
        curr=""
        l1=0
        l=0
        for i in s:
            if i in dict:
                l1=max(l,l1)
                dup=curr.index(i)
                curr=curr[dup+1:]+i
                dict={}
                for c in curr:
                    dict[c]=1
                l=len(curr)
            else:
                dict[i]=1
                curr+=i
                l+=1
        return max(l,l1)
        