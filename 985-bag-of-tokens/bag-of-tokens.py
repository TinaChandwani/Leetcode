class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if len(tokens) == 0:
            return 0
        tokens.sort()
        i = 0
        j = len(tokens) - 1
        score = 0
        max_score = 0

        while i <= j:
            if tokens[i] <= power:
                # face up
                score += 1
                power = power - tokens[i]
                max_score = max(max_score,score)
                i += 1
            elif score != 0 and tokens[i] > power:
                # face down from the last
                score -= 1
                power = power + tokens[j]
                max_score = max(max_score,score)
                j -= 1
            else:
                break
        return max_score 
