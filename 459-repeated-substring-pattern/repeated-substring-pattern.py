class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        con = (s + s)[1:-1]
        if s in con:
            return True
        return False