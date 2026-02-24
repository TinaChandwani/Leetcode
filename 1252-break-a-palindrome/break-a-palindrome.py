class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome) 
        if n == 1:
            return ""
        hasA = True
        ans = ''
        for i in range(len(palindrome)//2):
            if palindrome[i] != 'a':
                hasA = False
                ans = palindrome[:i] + 'a' + palindrome[i+1:]
                break
        if hasA == True:
            ans = palindrome[:n-1] + 'b'
        return ans