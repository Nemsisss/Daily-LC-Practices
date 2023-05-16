class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#         create a dictionary with the keys being each of the numbers in nums and values will be the #of occurances of each number in nums
        diction=Counter(nums)
        for i in range(len(nums)):
#             if the complement is among the keys of the dictionary and it does not have the same index as the current number, return the two complement numbers
            if  (target-nums[i]) in diction and i!=nums.index(target-nums[i]):
                return [i, nums.index(target-nums[i])]
            
# two slightly different approachs 
#1---------------------------------
#         hashmap = {}
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap:
#                 return [i, hashmap[complement]]
#             hashmap[nums[i]] = i

#2----------------------------------
        # hashmap = {}
        # for i in range(len(nums)):
        #     hashmap[nums[i]] = i
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in hashmap and hashmap[complement] != i:
        #         return [i, hashmap[complement]] 
