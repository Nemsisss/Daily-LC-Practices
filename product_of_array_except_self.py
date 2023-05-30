# import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#         toRet=[]
#         nums= np.array(nums)
#         for i, num in enumerate(nums):
#             if i==0:
#                 toRet.append(np.prod(nums[1:]))
#             elif i== len(nums)-1:
#                 toRet.append(np.prod(nums[0:i]))
#             else:
#                 toRet.append((np.prod(nums[0:i])) * (np.prod(nums[i+1:])))
#         return toRet

# another approach without using numpy
        length= len(nums)
        # initialize two empty arrays of size length
        left = [0]* length
        right=[0]*length
        toRet=[0]*length
        # since there are no elements to the left of the index 0 and no elements to the right of last index, initialize them to 1
        left[0]=1
        right[length-1]=1
        for i in range(1, length):
            left[i] = left[i-1] * nums[i-1]
        for i in range(length-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
        
        for i in range(length):
            toRet[i] = left[i]*right[i]
        return toRet

        
