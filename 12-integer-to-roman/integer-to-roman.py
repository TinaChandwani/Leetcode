class Solution:
    def intToRoman(self, num: int) -> str:
        intToRomanDict = {1000:"M", 900:"CM", 500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        answer = ""

        for i,symbol in intToRomanDict.items():
            while i <= num:
                answer += symbol
                diff = num - i
                num = diff
        return answer
            
