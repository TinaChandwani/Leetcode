class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        maxInt = 2**31 - 1

        while b != 0:
            add = (a ^ b) & mask
            carry = (a & b) & mask
            a = add
            b = (carry << 1) & mask
        
        if a <= maxInt:
            return a
        else:
            return ~(a ^ mask)