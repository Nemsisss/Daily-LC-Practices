class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        toRet=[]
        for i in candies:
            if i+extraCandies >= max(candies):
                toRet.append(True)
            else:
                toRet.append(False)
                
        return toRet
