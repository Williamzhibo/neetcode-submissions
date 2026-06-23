class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        seenS = {}
        seenT = {} 
        #dictionary for both, we will count characters 

        #by condition, s and t are same length
        for i in range(len(s)):
            #count every time we find the value
            seenS[s[i]] = 1 + seenS.get(s[i], 0)
            seenT[t[i]] = 1 + seenT.get(t[i], 0)

        return seenS == seenT
         

        