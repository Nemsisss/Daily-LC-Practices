class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # approach #1
        # nums1=list(set(nums1))
        # nums2=list(set(nums2))
        # toRet1=[i for i in nums1 if i not in nums2]
        # toRet2=[i for i in nums2 if i not in nums1]

        #approach #2
        # nums1=list(set(nums1))
        # nums2=list(set(nums2))
        # diction=Counter(nums1+nums2)
        # toBeRemoved=[i for i in diction if diction[i]==2]
        # for i in toBeRemoved:
        #     nums1.remove(i)
        #     nums2.remove(i)
        # return [nums1, nums2]

        #approach #3
        return [list(set(nums1)-set(nums2)),list(set(nums2)-set(nums1))]
