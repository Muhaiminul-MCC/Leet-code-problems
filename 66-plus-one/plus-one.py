class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = 0
        for digit in digits:
            nums = nums*10 + digit
        nums += 1
        final_list = [int(digit) for digit in str(nums)]
        return final_list

digits = [1, 2, 3]
solution = Solution()
solution.plusOne(digits)