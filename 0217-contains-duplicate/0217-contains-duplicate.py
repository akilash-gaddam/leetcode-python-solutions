class Solution(object):
    def containsDuplicate(self, nums):
        li=(set(nums))
        if len(li)!=len(nums):
            return True
        return False

        