class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left,right):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPalindrome(l+1,r) or isPalindrome(l,r-1)
        
        return True