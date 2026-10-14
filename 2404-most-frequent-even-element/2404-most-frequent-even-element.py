from collections import defaultdict
class Solution(object):
    def mostFrequentEven(self, nums):
        m=-1
        c=0
        n=-1
        for i in sorted(nums):
            if i % 2 == 0:
                c=nums.count(i)
                if c>m:
                    m=c
                    n=i
        return n