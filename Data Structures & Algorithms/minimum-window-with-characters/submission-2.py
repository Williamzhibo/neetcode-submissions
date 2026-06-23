class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '': return ''

        countT, window = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have, need = 0, len(countT)
        output, minLength = '', float('infinity')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if (c in countT and window[c] == countT[c]):
                have += 1
            
            while have == need:
                if (r - l + 1) < minLength:
                    output = s[l: r + 1]
                    minLength = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            
        return output