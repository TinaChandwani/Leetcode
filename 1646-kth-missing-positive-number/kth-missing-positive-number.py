class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        '''
        O(n) solution
        '''
        num = 1
        i = 0
        n = len(arr) - 1

        while i <= n:
            if arr[i] == num:
                i += 1
            else:
                k -= 1
                if k == 0:     
                    return num    
            num += 1
        return num + k - 1