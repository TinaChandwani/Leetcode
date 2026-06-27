class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        max_element = max(nums)
        min_element = min(nums)

        if max_element == min_element:
            return 0

        bsize = ceil((max_element - min_element) / (len(nums) - 1))
        bucket_count = (max_element - min_element) // bsize + 1
        bDict = defaultdict(list)
        maxArray = [float('-inf')] * bucket_count
        minArray = [float('inf')] * bucket_count
        ans = 0

        for i in range(len(nums)):
            buck_id = (nums[i] - min_element) // bsize
            bDict[buck_id].append(nums[i])
        
        for k,v in bDict.items():
            max_v = max(v)
            min_v = min(v)
            maxArray[k] = max_v
            minArray[k] = min_v 
        
        # Compare the min of the current bucket with the max of the previous non-empty bucket

        prev_max = min_element

        for i in range(bucket_count):
            # Skip empty buckets
            if minArray[i] == float('inf'):
                continue
            ans = max(ans, minArray[i] - prev_max)
            prev_max = maxArray[i]
        
        return ans