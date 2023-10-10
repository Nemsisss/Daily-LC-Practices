class Solution:
    def partitionString(self, s: str) -> int:
        # arr=[""]
        # count=0
        # for i in range(len(s)):
        #     if not s[i] in arr[count]:
        #         arr[count]+=s[i]
        #     else:
        #         count+=1
        #         arr.append(s[i])
        # return len(arr)
        seen_chars = set()
        count = 0
        
        for char in s:
            if char not in seen_chars:
                seen_chars.add(char)
            else:
                count += 1
                seen_chars = set(char)
            # print(seen_chars, count)
        
        return count + 1
