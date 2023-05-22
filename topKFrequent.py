class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diction = Counter(nums)
        sorted_list = sorted(diction.items(), key = lambda x:x[1], reverse = True)
        toReturn=[sorted_list[i][0] for i in range(k)]
        return toReturn
