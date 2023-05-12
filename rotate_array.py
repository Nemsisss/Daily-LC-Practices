class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """     
        n= len(nums)
        #to handle cases where k > len(sums)         
        k=k%n
        temp=nums[n-k:] + nums[:n-k]
        nums[:]=temp[:]
        
    # if done in place, with no extra memory:
        # n= len(nums)
        # # #to handle cases where k > len(sums)         
        # k=k%n
        # nums[n-k:]=nums[n-k:][::-1]
        # nums[:n-k]=nums[:n-k][::-1]
        # nums[:]= nums[::-1]
