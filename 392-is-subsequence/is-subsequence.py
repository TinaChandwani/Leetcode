class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if n1 == 0:
            return True
        if n2 == 0:
            return False
        if n1 == n2:
            if s == t:
                return True
            else:
                return False
        i = 0 
        j = 0
        while j < n2 :
            si = s[i]
            tj = t[j]
            if si == tj:
                i += 1
            if i == n1 :
                return True
            j += 1
        return False
        