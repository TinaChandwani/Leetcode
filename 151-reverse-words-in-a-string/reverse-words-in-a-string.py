class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        arr = s.split(" ")
        n = len(arr)
        ans = ""
        for i in range(n-1,-1,-1):
            if arr[i] == "":
                continue
            ans  = ans + " " + arr[i]
        ans = ans.strip()
        return ans