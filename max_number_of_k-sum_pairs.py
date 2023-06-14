class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # using hashtable (two-pass), O(n)
        count=0
        diction= Counter(nums)
        for i,num in enumerate(nums):
            if num <k and k-num in diction and diction[k-num]>=1 and diction[num]>=1:
                if not (k-num == num and diction[k-num]==1):
                    count+=1
                    if k-num==num:
                        diction[k-num]-=2
                    else:
                        diction[num]-=1
                        diction[k-num]-=1

        return count

        # using two-pointer O(nlogn)
        # nums.sort()
        # count=0
        # left=0
        # right=len(nums)-1
        # while left<right:
        #     if nums[left]+nums[right]<k:
        #         left+=1
        #     elif nums[left]+nums[right]>k:
        #         right-=1
        #     else:
        #         left+=1
        #         right-=1
        #         count+=1
        # return count
            
