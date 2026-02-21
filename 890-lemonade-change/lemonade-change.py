class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] in (10,20):
            return False
        fives = 0
        tens = 0
        for i in bills:
            if i == 5:
                fives += 1
            elif i == 10:
                if fives == 0:
                    return False
                fives -= 1
                tens += 1
            else:
                if fives > 0 and tens > 0:
                    fives -= 1
                    tens -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
                
                
        if fives < 0 or tens < 0:
            return False
        else:
            return True
        