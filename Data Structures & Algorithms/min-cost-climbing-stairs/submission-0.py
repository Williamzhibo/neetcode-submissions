class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        temp2, temp1 = 0, 0 # i - 2, and i - 1 respectively 

        for i in range(2, len(cost) + 1):
            temp2, temp1, = temp1, min(temp2 + cost[i-2], temp1 + cost[i-1])

        return temp1

        

        
            
