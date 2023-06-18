class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        #Dynamic sliding window
        start=0
        zeros=0
        maxLen=0

        for end in range(len(nums)):
            if nums[end]==0:
                zeros+=1
            while zeros>1:
                if nums[start]==0:
                    zeros-=1
                start+=1
            maxLen= max(maxLen,end-start)
            
        return maxLen
