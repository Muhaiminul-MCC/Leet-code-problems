class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_num = str(x)[::-1]  # Reverse the number as a string
        return  str(x) == reversed_num  # Compare the string versions

x = 121
solution = Solution()
print(solution.isPalindrome(x))
