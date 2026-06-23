class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #use the character counts as keys, add each element in given the keys 

        anagrams = defaultdict(list) # we will use the key to group each word. 

        for string in strs:
            key = [0] * 26

            for char in string:
                key[ ord(char) - ord("a") ] += 1 # count the letters in each string

            anagrams[tuple(key)].append(string)
            
        return list(anagrams.values())