class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def change(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if amount in memo:
                return memo[amount]

            min_count = float('inf')
            for coin in coins:
                res = change(amount - coin)
                if res != -1:
                    min_count = min(min_count, res + 1)

            memo[amount] = -1 if min_count == float('inf') else min_count
            return memo[amount]

        return change(amount)
