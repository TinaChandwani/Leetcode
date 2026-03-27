class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        n = len(nums)
        q = deque() # Decreasing order
        ans = []

        while r < n:
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if r - l + 1 > k:
                if q[0] == l:
                    q.popleft()
                l += 1
            
            if r - l + 1 == k:
                ans.append(nums[q[0]])
            r += 1
        
        return ans