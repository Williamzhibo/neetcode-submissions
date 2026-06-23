class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []

        anagrams = defaultdict(list) 

        for string in strs:
            key = [0] * 26
            for s in string:
                key[ord(s) - ord("a")] += 1
            anagrams[tuple(key)].append(string) # add each string into a list

        return list(anagrams.values())