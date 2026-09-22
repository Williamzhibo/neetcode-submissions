class Solution:
    def numDecodings(self, s: str) -> int:
        #at its core its kind of like our house robber problem/count 1/2
        #we are basically saying we either jump by 1 (single digit)
        #or we are jumping by 2 (multi-digit) 
        #whatever we choose, we need to 
        # for the DP problem decode ways, its almost identical to the add 1 or add 2 to get to your sum, except now if there is a 0, there is only one way to take the numbers?? so we treat it as if we are counting to a number, and sum the two ways that we can get to the number
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1

        ind2 = 1
        if s[1] == "0":
            ind1 = 0
        else: 
            ind1 = 1

        for i in range(1, len(s)): #need to stay within bounds
            temp = ind2
            ind2 = ind1 

            ind1 = 0
            if s[i] != "0":
                ind1 = ind1 + ind2
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                ind1 = ind1 + temp
        return ind1
