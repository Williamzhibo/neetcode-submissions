class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = [0] * 26
        window = [0] * 26
        k = len(need)

        for c in range(len(s1)):
            need[ord(s1[c]) - ord('a')] += 1 #all of s1
            window[ord(s2[c]) - ord('a')] += 1 #window from 0-len(s1) in s2

        matches = 0
        for i in range(26):
            matches += (1 if need[i] == window[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if (matches == 26): return True

            rindex = ord(s2[r]) - ord('a') #our right pointer's character index 
            window[rindex] += 1 
            if (need[rindex] == window[rindex]): matches += 1
            elif (need[rindex] + 1 == window[rindex]): matches -= 1

            lindex = ord(s2[l]) - ord('a') # our left pointers character index
            window[lindex] -= 1
            if (need[lindex] == window[lindex]): matches += 1
            elif (need[lindex] == window[lindex] + 1): matches -= 1
            l += 1
        return matches == 26