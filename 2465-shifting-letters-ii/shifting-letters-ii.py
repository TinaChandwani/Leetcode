class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff_arr = [0] * (n + 1)
        res = []

        for start,end,direction in shifts:
            if direction == 1:
                # Forward
                diff_arr[start] += 1
                diff_arr[end + 1] -= 1
            else:
                # backward
                diff_arr[start] -= 1
                diff_arr[end + 1] += 1 
        
        # Calculate prefix sum
        for i in range(1,n):
            diff_arr[i] += diff_arr[i-1]
        
        for i , ch in enumerate(s):
            new_char = chr((ord(ch) - ord('a') + diff_arr[i]) % 26 + ord('a'))
            res.append(new_char)
        
        return "".join(res)




        