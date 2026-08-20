class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Approach 2: using the constraint -> all lowercase letters
        '''

        groupDict = {}
        res = []

        for word in strs:
            group = [0] * 26
            for w in word:
                x = ord(w) - ord('a')
                group[x] += 1
            group = tuple(group)

            if group in groupDict:
                groupDict[group].append(word)
            else:
                groupDict[group] = [word]
        
        for v in groupDict.values():
            res.append(v)
        
        return res
