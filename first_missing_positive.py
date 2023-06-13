class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # If a positive integer is not in the given array it, the missing integer must be in the range [1..n]
    
        # using O(1) space and O(n)time
        originalLen=len(nums)
        # convert the array to a set, so that lookup will take O(1) time
        nums=set(nums)
        # if an integer is not missing then the answer is n+1.
        toRet= len(nums)+1
        # If an integer is missing it must be in the range [1..n]
        for i in range(1,originalLen+1):
            if i not in nums:
                return i
        return toRet



        


            
        
        
