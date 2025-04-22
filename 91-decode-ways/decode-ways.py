class Solution:
    def decoder(self,s,index,memo,count):
        # Base Condition
        if index == len(s):
            return 1
        
        if int(s[index]) == 0:
            return 0
        
        # Memoisation
        if index in memo:
            count = memo[index]
        else:
            count = count + self.decoder(s,index+1,memo,count)

            if len(s) > index + 1 and 10 <= int(s[index] + s[index+1]) <= 26:
                count = count + self.decoder(s,index+2,memo,count) 

            memo[index] = count
        return memo[index]

    def numDecodings(self, s: str) -> int:
        memo = {}
        count = 0
        return self.decoder(s,0,memo,count)
