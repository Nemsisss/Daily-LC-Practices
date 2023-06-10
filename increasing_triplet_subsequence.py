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
                return True 

        return False


        
