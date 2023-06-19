class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        uniquesLen= len(set(arr))
        diction={}
        for i in arr:
            if i not in diction:
                diction[i]=0
            else:
                diction[i]+=1
        return len(set(diction.values()))==uniquesLen

        # shorter approach
        # return len(set(Counter(arr).values()))==len(set(arr))
