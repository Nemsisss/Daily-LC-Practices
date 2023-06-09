class Solution:
    def compress(self, chars: List[str]) -> int:
    # two pointer approach

        curr=0
        uniques=0
        #since with a while loop we can increment curr by custom amounts after each iteration
        while curr < len(chars):
            group_length=1
            while group_length+curr < len(chars) and chars[group_length+curr]==chars[curr]:
                group_length+=1
            chars[uniques]=chars[curr]
            uniques+=1
            if group_length>1:
                split= list(str(group_length))
                chars[uniques:uniques+len(split)]= split
                uniques+=len(split)
            curr+=group_length

        return uniques

        #uses O(n) space
        # s=""
        # count=1
        # for i in range(len(chars)):
        #     if i==0:
        #         s+=chars[i]
        #     else:
        #         if chars[i]==chars[i-1]:
        #             count+=1
        #         else:
        #             if count>1:
        #                 s+= str(count)
        #             s+=chars[i]
        #             count=1
        # # append the last count if greater than 1
        # if count>1:
        #     s+= str(count)
        # for i in range(len(s)):
        #     chars[i]=s[i]
        
        # return len(s)
        






