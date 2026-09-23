import math 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        seen = {} #mapping ammounts to minimum cound values
    
        def DP (remaining): 
            if remaining == 0:
                return 0

            if remaining < 0: 
                return math.inf

            if remaining in seen: 
                return seen[remaining]

            best = math.inf #start with infinity but we can check everything
            for coin in coins: 
                best = min(best, 1 + DP(remaining - coin)) #either add or dont add the coin

            seen[remaining] = best
            return best 

        result = DP(amount)
        return result if result != math.inf else -1
