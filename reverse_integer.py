class Solution:
    def reverse(self, x: int) -> int:
        #approach 1
        temp=x
        if x==0:
            return x
        if x<0:
            temp*= -1
        reverse= int(str(temp)[::-1])
        if( reverse > 2**31-1) or reverse < -2**31:
            return 0
        if x<0:
            reverse*= -1
        return reverse
    
    #approach 2
#         reversed=""
#         temp=x
#         if x==0:
#             return x
#         if x<0:
#             temp*= -1

#         while temp >=1:
#             reversed+= (str)(temp%10)
#             temp= math.floor(temp/10)

#         toReturn= int(reversed)
#         if x<0:
#             toReturn*= -1

#         if( toReturn > 2**31-1) or toReturn < -2**31:
#             return 0

#         return toReturn
