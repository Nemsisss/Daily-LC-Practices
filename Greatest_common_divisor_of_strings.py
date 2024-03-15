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


########### JS SOLUTION ###########
# /**
#  * @param {string} str1
#  * @param {string} str2
#  * @return {string}
#  */
# var gcdOfStrings = function(str1, str2) {
#     if (str1+str2 != str2+str1)
#     {
#         return "";
#     }
#     let index=0;
#     for(let i=1; i<= Math.min(str1.length, str2.length); i++)
#     {
#         if(str1.length %i==0 && str2.length%i==0)
#         {
#             index=i;
#         }
#     }
#     return str1.substr(0, index);
# };
