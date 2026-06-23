class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i): #current index we are starting with
            if i >= len(s):
                res.append(part.copy())
                return 
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j): #case is we hit our palindrome so we will kill it and move on 
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[r] != s[l]:
                return False
            l, r = l + 1, r - 1
        
        return True
