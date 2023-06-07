class Solution:
    def compress(self, chars: List[str]) -> int:
        s=""
        count=1
        for i in range(len(chars)):
            if i==0:
                s+=chars[i]
            else:
                if chars[i]==chars[i-1]:
                    count+=1
                else:
                    if count>1:
                        s+= str(count)
                    s+=chars[i]
                    count=1
        # append the last count if greater than 1
        if count>1:
            s+= str(count)
        for i in range(len(s)):
            chars[i]=s[i]
        
        return len(s)


