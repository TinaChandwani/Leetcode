class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        if p == '*':
            return True
        i = 0
        j = 0
        n,m = len(s), len(p)

        while i < n and j < m:
            if p[j] == '*':
                end_p = p[j+1:]
                end_s = s[i:]
                if end_p in end_s:
                    return True
                else:
                    i = i - j + 1
                    j = 0
                    continue
            if s[i] != p[j]:
                i = i - j + 1
                j = 0 
            elif s[i] == p[j]:
                i += 1
                j += 1
        
        if j == m:
            return True

        if j < m and p[j] == '*':
            end_p = p[j+1:]
            return end_p == ''

        return False
        
       