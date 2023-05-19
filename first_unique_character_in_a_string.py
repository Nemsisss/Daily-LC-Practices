class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr= [i for i in s]
        diction= Counter(arr)
        for i in diction:
            if diction[i]==1:
                return s.index(i)
        return -1
