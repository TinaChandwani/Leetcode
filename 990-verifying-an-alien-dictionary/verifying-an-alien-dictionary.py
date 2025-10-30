from collections import defaultdict

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = defaultdict(int)
        for i in range(len(order)):
            rank[order[i]] += i
        
        print(f'rank {rank}')

        def twoWords(w1,w2):
            print(f'in')
            nonlocal rank
            minLen = min(len(w1),len(w2))
            for i in range(minLen):
                print(f'w1[i] {w1[i]} w2[i] {w2[i]}')
                if w1[i] != w2[i]:
                    r1 = rank[w1[i]]
                    r2 = rank[w2[i]]
                    print(f'r1 {r1} r2 {r2}')
                    if r1 > r2:
                        return False
                    else:
                        return True
            return len(w1) <= len(w2)
        
        n = len(words)
        k = 0
        while k < n - 1:
            ans = twoWords(words[k],words[k+1])
            if ans == False:
                return False
            k += 1
        return ans