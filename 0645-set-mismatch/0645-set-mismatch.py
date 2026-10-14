class Solution(object):
    def findErrorNums(self, nums):
        dict={}
        dup=miss=None
        for i in nums:
            dict[i]=dict.get(i,0)+1
        for i in range(1,len(nums)+1):
            if dict.get(i,0)==2:
                dup=i
            elif dict.get(i,0)==0:
                miss=i
        return [dup,miss]
