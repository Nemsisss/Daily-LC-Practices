class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         TWO-POINTER
#         to keep track of the non-zero indices in the modified array
        nonZ=0
        for i in range(len(nums)):
            if nums[i]!=0 :
                nums[nonZ]=nums[i]
                if nonZ!=i:
                    nums[i]=0
                nonZ+=1
