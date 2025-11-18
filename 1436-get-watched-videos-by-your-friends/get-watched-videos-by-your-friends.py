from collections import deque
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        '''
        We use BFS here, because we need to find the shortest path (This is the
        hint here)
        '''
        q = deque()
        q.append(id)
        current_level = 0
        visit = set()
        visit.add(id)
        ans = []

        while q and current_level < level:
            l = len(q)
            for i in range(l):
                f = q.popleft()
                for nei in friends[f]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
            current_level += 1
        
        freq = defaultdict(int)
        for p in q:
            for v in watchedVideos[p]:
                freq[v] += 1
        sort_freq = dict(sorted(freq.items(), key = lambda x: (x[1],x[0])))
        for j in sort_freq.keys():
            ans.append(j)
        return ans