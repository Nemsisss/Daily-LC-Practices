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
