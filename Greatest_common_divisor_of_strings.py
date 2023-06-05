class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shorter= str2 if len(str2)<= len(str1) else str1
        longer = str2 if len(str2)>len(str1) else str1
        for index in range(len(shorter),0,-1):
            temp=""
            prefix= shorter[:index]
            if len(longer)%index==0 and len(shorter)%index==0:
                if prefix* (len(longer)//index) == longer and prefix* (len(shorter)//index)== shorter:
                    return prefix

        return ""
