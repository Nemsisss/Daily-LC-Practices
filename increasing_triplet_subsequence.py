class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min = float("inf")
        second_min = float("inf")
        for i in nums:
            if first_min >= i :
                first_min=i
            elif  second_min >=i:
                second_min=i
            else:
                print(first_min, second_min)
                return True 

        return False

        # DP, exceeds time limit
        # n = len(nums)
        # dp = [1] * n
        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j]+1)
        #             if dp[i]>=3:
        #                 return True
        # return False


  
        
