class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        un_num = len(nums)
        J = 1

        for i in range(1, un_num):
            if nums[i] != nums[i-1]:
                nums[J] = nums[i]
                J += 1

        return J