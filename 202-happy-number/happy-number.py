class Solution:
    def happy(self,happyDict,n):
        happySum = 0
        for digit in str(n):
            digit = int(digit)
            if digit in happyDict:
                squareDigit = happyDict[digit]
            else:
                squareDigit = digit * digit
            happySum += squareDigit
        return happySum

    def isHappy(self, n: int) -> bool:
        happyDict = {}
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.happy(happyDict,n)
        
        if n == 1:
            return True
        else:
            return False

        
