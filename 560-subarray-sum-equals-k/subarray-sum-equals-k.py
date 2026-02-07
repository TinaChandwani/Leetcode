class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int) # prefix : count
        currSum = 0
        count = 0
        n = len(nums)

        for i in range(n):
            currSum += nums[i] 
            if currSum == k:
                count += 1
            diff = currSum - k
            if diff in prefix:
                count += prefix[diff]
            prefix[currSum] += 1
        return count

