class Solution(object):
    def longestCommonPrefix(self, strs):
        
        for i in range(len(strs[0])):
            for string in strs:
                
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        
        return strs[0]

strs = ["flower", "flow", "flight"]
solution = Solution()
print(solution.longestCommonPrefix(strs))
