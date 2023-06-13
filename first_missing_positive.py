class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # If a positive integer is not in the given array it, the missing integer must be in the range [1..n]
        # So, If an integer is missing it must be in the range [1..n], if an integer is not missing then the answer is n+1.

        #O(1) space and O(n) time
        # sumWithoutMissing= 0
        # sumWithMissing=0
        # for i in range(1,len(nums)+1):
        #     if nums[i-1]>0:
        #         sumWithMissing+= nums[i-1]
        #     sumWithoutMissing+=i
        # print(sumWithoutMissing, sumWithMissing)
        # return 1
        
        # using O(n) space and O(n)time
        numsSet=set(nums)
        toRet= len(nums)+1
        for i in range(1,len(nums)+1):
            if i not in numsSet:
                return i
        return toRet



        


            
        
        
