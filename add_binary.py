class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # revA=[int(i) for i in a ][::-1]
        # revB=[int(i) for i in b ][::-1]
        # while len(revB)<len(revA) :
        #     revB.append(0)
        # while len(revB)>len(revA) :
        #     revA.append(0)
        # carry=0
        # toRet=[]
        # for i in range(len(revA)) :
        #     if (revA[i]+revB[i]+carry) > 1:
        #         toRet.append( str((revA[i]+revB[i]+carry)%2))
        #         carry=1
        #     else:
        #         toRet.append(str(revA[i]+revB[i]+carry))
        #         carry=0

        # if carry:
        #     toRet.append(str(1))

        # return "".join(toRet[::-1])

        # using bin()
        a=int(a,2)
        b=int(b,2)
        return bin(a+b)[2:]

