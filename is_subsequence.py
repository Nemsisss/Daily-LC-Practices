class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # TWO-POINTER
        if len(t)<len(s):
            return False
        elif len(s)==0:
            return True
        sIter=0
        for i in range(len(t)):
            if sIter<len(s) and t[i]==s[sIter]:
                sIter+=1
                if sIter==len(s):
                    return True
        return False
