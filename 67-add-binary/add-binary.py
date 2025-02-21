class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2)
        num2 = int(b, 2)
        sum_num = num1 + num2
        num_bin = bin(sum_num)[2:]
        final_res = str(num_bin)
        return final_res


a = "11"
b = "1"
solution = Solution()
solution.addBinary(a, b)