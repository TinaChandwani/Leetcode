class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Approach 1 : Sort every string
        sorted string : {strings}
        aet : {eat,tea,ate}
        TC : k(nlogn) n is max len(string) and k is number of strings
        '''

        sDict = {}
        res = []

        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i not in sDict:
                sDict[sorted_i] = [i]
            else:
                sDict[sorted_i].append(i)
        
        for k in sDict.values():
            res.append(k)
        
        return res