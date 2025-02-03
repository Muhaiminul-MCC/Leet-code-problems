class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to store Roman numeral values
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        prev_value = 0

        # Iterate through the string in reverse
        for char in reversed(s):
            # print(char)
            curr_value = roman_values[char]

            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value

            prev_value = curr_value

        return total


# Example usage
s = "III"
solution = Solution()
print(solution.romanToInt(s))
