class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineDict = defaultdict(int)
        for i in magazine:
            magazineDict[i] += 1
        
        for j in ransomNote:
            if j not in magazineDict.keys() or magazineDict[j] == 0:
                return False
            else:
                magazineDict[j] -= 1
        return True
            