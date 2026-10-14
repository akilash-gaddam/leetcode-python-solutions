import random
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def qsort(nums):
            if len(nums)<=1:
                return nums
            pivot=random.choice(nums)
            left=[x for x in nums if x < pivot]
            middle=[x for x in nums if x == pivot]
            right=[x for x in nums if x > pivot]

            return qsort(left)+middle+qsort(right)
        return qsort(nums)

        