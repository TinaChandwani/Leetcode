class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        '''
        We need to store the next consonants for every element
        '''
        n = len(word)
        count = [n] * n
        last_cons = n
        ans = 0
        c = 0
        vDict = defaultdict(int)
        l = 0
        r = 0

        for i in range(n-1,-1,-1):
            count[i] = last_cons
            if word[i] not in ('a','e','i','o','u'):    
                last_cons = i
        
        while r < n:
            if word[r] in ('a','e','i','o','u'):
                vDict[word[r]] += 1
            else:
                c += 1

            while c > k:
                if word[l] in ('a','e','i','o','u'):
                    vDict[word[l]] -= 1
                    if vDict[word[l]] == 0:
                        del vDict[word[l]]
                else:
                    c -= 1
                l += 1
            
            while len(vDict) == 5 and c == k:
                # valid 
                idx = count[r] # it will tell me next consonant after jth index
                ans += (idx - r)
                if word[l] in ('a','e','i','o','u'):
                    vDict[word[l]] -= 1
                    if vDict[word[l]] == 0:
                        del vDict[word[l]]
                else:
                    c -= 1
                l += 1
            r += 1
        
        return ans