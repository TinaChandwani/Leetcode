class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        ans = 0 
        i = len(s) - 1
        while i >= 0:
            present = symbols[s[i]]
            if i != 0:
                future = symbols[s[i-1]]
                if present > future:
                    ans += (present - future)
                    i = i - 2
                else:
                    ans += present
                    i = i - 1
            else:
                ans += present
                i = i - 1
        return ans

