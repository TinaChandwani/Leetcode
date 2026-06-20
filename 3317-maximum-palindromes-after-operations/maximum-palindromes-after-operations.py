class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        wordsDict = defaultdict(int)
        wordsArr = []
        total_pairs = 0
        ans = 0

        for word in words:
            wordsArr.append(len(word))
            for char in word:
                wordsDict[char] += 1
        
        for v in wordsDict.values():
            total_pairs += v // 2

        wordsArr.sort()

        for w in wordsArr:
            need_pairs = w // 2
            if total_pairs >= need_pairs:
                ans += 1
                total_pairs -= need_pairs
            else:
                break
        
        return ans
            


