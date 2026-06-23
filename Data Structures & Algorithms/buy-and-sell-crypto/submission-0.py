class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxJump = 0
        m = prices[0]
        for i in range(len(prices)):
            maxJump = max(maxJump, prices[i] - m)
            if m > prices[i]:
                m = prices[i]
        return maxJump
            