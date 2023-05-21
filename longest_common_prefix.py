class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest= min(strs, key=len)
        prefix=""
        for i in range(len(shortest)):
            for word in strs:
                if shortest[i]!=word[i]:
                    return prefix
            prefix+=shortest[i]
        return prefix
