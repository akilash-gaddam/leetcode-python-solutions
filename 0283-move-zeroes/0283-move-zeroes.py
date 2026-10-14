class Solution(object):
    def moveZeroes(self, nums):
        c=nums.count(0) 
        nums[:]=[n for n in nums if n !=0 ]
        return nums.extend([0]*c)
        