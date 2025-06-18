class Solution:
    # def happy(self,happyDict,n):
    #     happySum = 0
    #     for digit in str(n):
    #         digit = int(digit)
    #         if digit in happyDict:
    #             squareDigit = happyDict[digit]
    #         else:
    #             squareDigit = digit * digit
    #         happySum += squareDigit
    #     return happySum

    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        
        return n == 1