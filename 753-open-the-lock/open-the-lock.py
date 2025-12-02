class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        '''
        BFS 
        '''
        deadends = set(deadends)
        print(f'de {deadends}')
        if target == '0000':
            return 0
        if target in deadends or '0000' in deadends:
            return -1
        q = deque()
        q.append(('0000',0)) # Starting Point, levels
        

        while q:
            lock,moves = q.popleft()
            if lock == target:
                return moves
            for i in range(4):
                ch = int(lock[i])
                inc = (ch + 1) % 10
                new_chr = lock[:i] + str(inc) + lock[i+1:]
                if new_chr not in deadends:
                    q.append((new_chr,moves+1))
                    deadends.add(new_chr)
                if ch == 0:
                    dec = 9
                else:
                    dec = ch - 1
                dec_chr = lock[:i] + str(dec) + lock[i+1:]
                if dec_chr not in deadends:
                    q.append((dec_chr,moves+1))
                    deadends.add(dec_chr)
        return -1