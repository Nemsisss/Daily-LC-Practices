class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        temp=0
        for i in nums:
            if i:
                temp+=1
            else:
                temp=0
            if temp>max:
                max=temp
        return max
