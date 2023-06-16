class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result= sum(nums[:k])/k
        maxAvg=result
        for i in range(1,len(nums)-k+1):
            result=result-(nums[i-1]/k)+(nums[i+k-1]/k)
            maxAvg=max(maxAvg, result)
            
        return maxAvg
