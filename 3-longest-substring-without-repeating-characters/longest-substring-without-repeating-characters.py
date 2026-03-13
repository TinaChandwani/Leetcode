class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        n = len(s)
        l = 0
        r = 0
        active = set()
        ans = 0

        while r < n:
            while l < r and s[r] in active:
                active.remove(s[l])
                l += 1
            active.add(s[r])
            ans = max(ans, r - l + 1)
            r += 1
        return ans
