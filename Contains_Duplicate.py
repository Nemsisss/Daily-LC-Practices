class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newLen= len(set(nums))
        return not newLen == len(nums)
