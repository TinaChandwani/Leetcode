class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        Time Complexity = (2^n * n)
        '''
        def isPalindrome(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True
            
        def backtrack(idx,curr,res):
            if idx == len(s):
                res.append(curr[:])
            
            for i in range(idx,len(s)):
                if isPalindrome(idx,i):
                    curr.append(s[idx:i+1])
                    backtrack(i + 1, curr,res)
                    curr.pop()
            
            return res
        
        return backtrack(0,[],[])