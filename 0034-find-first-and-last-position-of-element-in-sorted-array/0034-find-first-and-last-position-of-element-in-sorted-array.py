class Solution(object):
    def searchRange(self, nums, target):
        r=[-1,-1]
        if target in nums:
            r[0]=nums.index(target)
            nums.reverse()
            r[1]=len(nums)-nums.index(target)-1
        return r
                    