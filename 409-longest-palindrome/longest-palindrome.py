class Solution:
    def longestPalindrome(self, s: str) -> int:
        pDict = defaultdict(int)
        ans = 0
        for i in s:
            pDict[i] += 1
        print(f'pdict {pDict}')

        if len(pDict) == 1:
            return len(s)
        
        for k, v in pDict.items():
            if v % 2 == 0:
                ans += v
            else:
                ans += (v-1)
        if ans == len(s):
            return ans
        else:
            return ans + 1