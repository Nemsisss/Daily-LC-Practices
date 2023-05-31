class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return chain.from_iterable(combinations(nums, i) for i in range(len(nums)+1))

# backtracking approach
        # def backtrack(start, subset):
        #     res.append(subset[:])
        #     for i in range(start, len(nums)):
        #         subset.append(nums[i])
        #         backtrack(i + 1, subset)
        #         subset.pop()
                
        # res = []
        # backtrack(0, [])
        # return res



