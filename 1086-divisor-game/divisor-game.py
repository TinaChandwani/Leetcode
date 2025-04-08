class Solution:
    def divisorGame(self, n: int) -> bool:
        '''
        Break points -> n - x should not be 1
        base case -> if n== 1 return false
        '''

        if n % 2 == 0:
            return True
        else:
            return False