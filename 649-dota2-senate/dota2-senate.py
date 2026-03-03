class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_q = deque()
        d_q = deque()
        n = len(senate)

        for i in range(n):
            if senate[i] == 'R':
                r_q.append(i)
            else:
                d_q.append(i)
        while len(r_q) > 0 and len(d_q) > 0:
            r_index = r_q.popleft()
            d_index = d_q.popleft()
            if r_index < d_index:
                # d is banned r acts first
                r_q.append(r_index + n)
            else:
                d_q.append(d_index + n)
        if len(r_q) == 0:
            return "Dire" 
        else:
            return "Radiant"      

