class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        memo = {} # memo[(i, op1, op2)] = minimum_sum_from_i
        def solve(k,op1,op2,i):
            key = (i,op1,op2)
            if key in memo:
                return memo[key]
            if i >= len(nums):
                return 0
            # Case 0: DO NOTHING
            result = nums[i] + solve(k,op1,op2,i+1)
            key = (i,op1,op2)
            memo[key] = result
            # Case 1: Apply only op1
            if op1 > 0:
                newValue = (nums[i] + 1) // 2
                onlyOp1 = newValue + solve(k,op1-1,op2,i+1)
                result = min(result,onlyOp1)
                key = (i,op1,op2)
                memo[key] = result
            
            # Case 2: Apply only op2
            if (op2 > 0) and nums[i] >= k:
                newVal = nums[i] - k
                onlyOp2 = newVal + solve(k,op1,op2-1,i+1)
                result = min(result,onlyOp2)
                key = (i,op1,op2)
                memo[key] = result
            
            # Case 3: Apply op1 -> op2
            if op1 > 0 and op2 > 0:
                new = (nums[i] + 1) // 2
                if new >= k:
                    new2 = new - k
                    n = new2 + solve(k,op1-1,op2-1,i+1)
                    result = min(result,n)
                    key = (i,op1,op2)
                    memo[key] = result
            
            # Case 4: Apply op2 -> op1:
            if op1 > 0 and op2 > 0 and nums[i] >= k:
                n1 = nums[i] - k
                n2 = (n1 + 1) // 2
                n3 = n2 + solve(k,op1-1,op2-1,i+1)
                result = min(result,n3)
                key = (i,op1,op2)
                memo[key] = result
            
            return memo[key]
        
        return solve(k,op1,op2,0)
