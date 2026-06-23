class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hset = set()
        maxLength = 0
        l = 0
        for r in range(len(s)):
            while s[r] in hset:
                hset.remove(s[l])
                l += 1
            hset.add(s[r])
            maxLength = max(maxLength, len(hset))
        return maxLength
            
                