class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels= set(['a','e','i','o','u'])
        s=list(s)
        diction={}
        for i,letter in enumerate(s):
            if letter.lower() in vowels:
                diction[i]=letter
        # reverse the keys (indices) only 
        new_dict= {key: value for key, value in zip(reversed(diction.keys()), diction.values())}
        for i in new_dict:
            s[i]=new_dict[i]

        return ''.join(s)
########## Javascript ##########
    # let vowels= new Set(['a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O', 'U']);
    # let str= [...s];
    # let left=0;
    # let right=s.length-1;
    
    # while(left<right)
    # {
    #     if(!vowels.has(str[left]))
    #     {
    #         left+=1;
    #     }
    #     if(!vowels.has(str[right]))
    #     {
    #         right-=1;
    #     }
    #     if(vowels.has(str[right]) && vowels.has(str[left]))
    #     {
    #         let temp=str[left];
    #         str[left]=str[right];
    #         str[right]=temp;
    #         left+=1;
    #         right-=1;
    #     }
    # }
    # return str.join('');
