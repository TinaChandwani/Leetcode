class Solution:
    def addMinimum(self, word: str) -> int:
        s = 'abc'
        i = 0
        j = 0
        n = len(word)
        cost = 0

        while j < n:
            if i == 3:
                i = 0
            if s[i] != word[j]:
                cost += 1
            else:
                j += 1
            i += 1

        return cost + (3 - i)
