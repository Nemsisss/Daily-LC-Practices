class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        limit= min(len(word1), len(word2))
        toRet=""
        for i in range(limit):
            toRet+= word1[i]+word2[i]
        if limit==len(word1):
            toRet+= word2[i+1:]
        else:
            toRet+= word1[i+1:]

        return toRet
