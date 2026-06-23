class Solution:
    def isPalindrome(self, s: str) -> bool:
        removed = ""

        for character in s:
            if (character.isalnum()):
                removed += character

        for i in range (len(removed)//2):
            if (removed[i].lower() != removed[(len(removed) - i) - 1].lower()):
                return False
        return True