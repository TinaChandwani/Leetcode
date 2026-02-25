class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        pDict = defaultdict(int)
        ans = 0
        hasMid = False

        for i in words:
            pDict[i] += 1

        for j in words:
            reverse = j[::-1]
            if j != reverse:
                # ab -> ba
                if reverse not in pDict:
                    continue
                else:
                    if pDict[reverse] > 0 and pDict[j] > 0:
                        pDict[j] -= 1
                        pDict[reverse] -= 1
                        ans += 4
            else:
                # aa -> aa   
                if pDict[j] >= 2:
                    ans += 4
                    pDict[j] -= 2
                else:
                    if pDict[j] == 1 and hasMid == False:
                        ans += 2
                        pDict[j] -= 1
                        hasMid = True
        return ans
