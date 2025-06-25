class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return list(set(nums))
        topDict = defaultdict(int)
        answer = []
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for i in nums:
            topDict[i] += 1

        for j,ke in topDict.items():
            bucket[ke].append(j)
        
        for _ in range(len(nums),0,-1):
            for num in bucket[_]:
                answer.append(num)
                if len(answer) == k:
                    return answer