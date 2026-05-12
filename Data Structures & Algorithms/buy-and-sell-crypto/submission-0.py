class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        target = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                diff = prices[j] - prices[i]
                if target < diff:
                    target = diff
        
        return target

        