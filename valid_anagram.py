class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#         if len(t)<len(s):
#             return False
#         sArr=[i for i in s]
#         sDict=Counter(sArr)
#         for i in t:
#             if sDict[i]>0:
#                 sDict[i]-=1
#             else:
#                 return False
            
#         return True
        return Counter(s)==Counter(t)
