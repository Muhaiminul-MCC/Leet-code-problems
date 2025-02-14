from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid+1
            elif nums[mid]>target:
                r = mid-1
            else:
                return mid
        if nums[mid] < target:
            return mid + 1
        else:
            return mid

nums = [1,3,5,6]
target = 5
solution = Solution()
result = solution.searchInsert(nums, target)
print(result)
