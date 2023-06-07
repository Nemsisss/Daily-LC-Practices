class Solution:
    def reverseWords(self, s: str) -> str:
        toRet= s.split()[::-1]
        return " ".join(toRet)
