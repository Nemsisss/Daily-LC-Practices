class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        toReturn=[]
        smallerList= nums1 if len(nums1)<len(nums2) else nums2
        dict=Counter(smallerList) 
        for key in dict:
            if (smallerList==nums1 and key in nums2) or (smallerList==nums2 and key in nums1):
                lim=min(nums1.count(key), nums2.count(key))
                for i in range(lim):        
                    toReturn.append(key)
        return toReturn
    

#     TWO-POINTER APPROACH
#         i = 0
#         j = 0
#         res = []
#         nums1.sort()
#         nums2.sort()

#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] == nums2[j]:
#                 res.append(nums1[i])
#                 i += 1
#                 j += 1
#             elif nums1[i] < nums2[j]: 
#                 i += 1
#             else:
#                 j += 1
#         return res
