class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lastInd=len(digits)-1
        curr= digits[lastInd]
        carry=0
        if curr !=9:
            digits[lastInd]+=1
        else:
            carry=1
            while lastInd>=0 and carry==1:
                if digits[lastInd]+1 > 9:
                    carry=1
                else:
                    carry=0
                digits[lastInd]+=1
                digits[lastInd] %=10
                lastInd-=1
        if carry==1 :
            digits.insert(0,1)
        return digits
