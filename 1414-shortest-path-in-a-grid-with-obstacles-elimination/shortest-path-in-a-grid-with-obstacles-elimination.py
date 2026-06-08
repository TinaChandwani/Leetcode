class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        visit = set()
        q = deque()
        q.append((0, 0, k))
        visit.add((0, 0, k))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        steps = 0
        n = len(grid)
        m = len(grid[0])

        while q:
            for _ in range(len(q)):
                r, c, remk = q.popleft()
                if r == n - 1 and c == m - 1:
                    return steps
                for i, j in directions:
                    new_r = r + i
                    new_c = c + j

                    if (
                        0 <= new_r < n
                        and 0 <= new_c < m
                    ):
                        new_remk = remk - grid[new_r][new_c]
                        if new_remk >= 0 and (new_r,new_c,new_remk) not in visit:
                            visit.add((new_r,new_c,new_remk))
                            q.append((new_r,new_c,new_remk))
            steps += 1
        return -1
