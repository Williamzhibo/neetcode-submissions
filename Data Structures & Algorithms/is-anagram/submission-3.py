class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 3 ways to solve this. 
        # 1) sort the lists, compare if equal. nlogn + mlogm average time assuming timsort, 1 or n space 
        # 2) Hashmap counting every character, then comparing counts at the end. n + m time, 1 space assuming max 26 characters
        # 3) essentially 2, except we explicitly allocate 26 positions 

        if len(s) != len(t):
            return False

        sets = {}
        sett = {}

        for i in range(len(s)):
            sets[s[i]] = 1 + sets.get(s[i], 0) #get gives us 0 if it doesnt exist
            sett[t[i]] = 1 + sett.get(t[i], 0)
        
        for key in sets:
            if (sets[key] != sett.get(key,0)):
                return False 
        return True