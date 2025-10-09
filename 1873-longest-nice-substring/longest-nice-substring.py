class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        '''
        Solving using Divide and Conquer
        Find the bad character in the string (A bad character is the
        one which does not have its corresponding lower
        or uppercase)
        The bad character is then your pivot and you divide the str
        left and right accordingly
        Conquer -> keep on dividing recursively on all left and rig
        str and return left if len(left) >= len(right) else right

        Learned:
        swapcase() -> swaps the case of the letters in python
        '''
        # Base condition
        if len(s) < 2:
            return ""
        char = set(s) # Will remove all the duplicates
        for i in range(len(s)):
            if s[i].swapcase() not in char:
                # Basically bad character
                # Now divide left and right
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                if len(left) >= len(right):
                    return left
                else:
                    return right
        return s #The whole string is nice
