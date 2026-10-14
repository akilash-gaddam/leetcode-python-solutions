class Solution(object):
    def runningSum(self, nums):
        l=[]
        s=0
        for i in nums:
            s+=i
            l.append(s)
        return l
        