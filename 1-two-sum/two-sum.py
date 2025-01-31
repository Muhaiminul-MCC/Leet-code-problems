class Solution:

    def twoSum(self, nums, target):
        # Main code
        dic = {}

        for i,num in enumerate(nums):
            if target - num in dic:
                return[dic[target - num],i]
            dic[num] = i
        return[]


nums = [2,7,11,15]
target = 9 # Target number
solution = Solution()
print(solution.twoSum(nums, target))
