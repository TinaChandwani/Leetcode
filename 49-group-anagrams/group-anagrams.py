class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupDict = {}
        output = []
        n = len(strs)

        for i in range(n):
            word = strs[i]
            group = [0] * 26
            for j in word:
                x = ord(j) - ord('a')
                group[x] += 1
            group = tuple(group)
            if group in groupDict.keys():
                groupDict[group].append(word)
            else:
                groupDict[group] = [word]
        
        for j in groupDict.values():
            output.append(j)
        
        return output