class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

# DYNAMIC SLIDING WINDOW APPROACH 
        start=0
        maxLen=0
        zeros=0

        for end in range(len(nums)):
            if nums[end]==0:
                zeros+=1
            while zeros>k:
                if nums[start]==0:
                    zeros-=1
                start+=1
            maxLen=max(maxLen, end-start+1)
            
        return maxLen
