class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs:
            res += str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        decoded, i = [], 0

        while i < len(s):
            j = i # i is beginning index of where number is here

            while s[j] != "#":
                j += 1
            # j is now at the length 
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded.append(s[i:j])
            i = j
        return decoded



