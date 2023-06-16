class Solution:
    def maxVowels(self, s: str, k: int) -> int:
    
#     SLIDING WINDOW APPROACH
        vowels=set(['a','e','i','o','u'])
        substr=s[:k]
        count=0     
        for i in substr:
            if i in vowels:
                count+=1
        maxCount= count
        for i in range(1, len(s)-k+1):
            if s[i-1] in vowels and s[i+k-1] not in vowels:
                count-=1
            elif s[i-1] not in vowels and s[i+k-1] in vowels:
                count+=1
            maxCount=max(maxCount,count)
        return maxCount
