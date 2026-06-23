class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #generate a hashset of seen characters, as soon as we find a duplicate, store the value of the length, then reset and continue 

        #seen characters

        #count = 0 
        # as we see characters, we add to our running count, as soon as we see the duplicate, we return that and call it a day 
        seen = set()
        longest = 0
        lp = 0
        rp = 0 
        while rp < len(s): 
            if s[rp] not in seen: 
                seen.add(s[rp])
                longest = max(rp - lp + 1, longest)
                rp += 1
            else: 
                while s[lp] != s[rp]: #after this s[lp] == s[rp]
                    seen.remove(s[lp])
                    lp += 1 
                    #xyzadfsafdsa
                seen.remove(s[lp])
                lp += 1
                
                #now we know we're valid? 
                # We don't need to update longest here, the logic above handles it

        return longest