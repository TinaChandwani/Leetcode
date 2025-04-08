class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        wordList = defaultdict(int)
        groudTruth = defaultdict(int)
        left = 0
        right = 0
        n = len(s)
        plen = len(p)
        output = []
        # Base Case
        if len(p) > len(s):
            return []
        
        for ch in p:
            groudTruth[ch] += 1
        
        while right < n:
            wordList[s[right]] += 1
            if right - left + 1 > plen:
                wordList[s[left]] -= 1
                if wordList[s[left]] == 0:
                    del wordList[s[left]]
                left += 1
            if right - left + 1 == plen:
                if wordList == groudTruth:
                    output.append(left)
            right += 1
        
        return output