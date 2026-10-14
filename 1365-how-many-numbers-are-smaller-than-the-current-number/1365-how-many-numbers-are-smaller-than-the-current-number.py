class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        c=0
        l=[]
        for i in nums:
            for j in nums:
                if i>j:c+=1
            l.append(c)
            c=0
        return l
        