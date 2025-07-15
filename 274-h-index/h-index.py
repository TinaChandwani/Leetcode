class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        U -> n cannot be a negative integer
        M -> 
        I ->
        1) Sort the array in decending order
        2) check if citations[i] >= i + 1 (array is 0 indexed)
        3) update hindex accordlingly 
        OR
        1) Create a Dictionary
        2) Update the frequency count for each number
        3) Iterate Backwards and count until it surpasses the i
        """

        n = len(citations)
        hDict = defaultdict(int)
        total = 0

        for i in citations:
            hDict[min(i,n)] += 1
        
        for h in range(n,-1,-1):
            total += hDict[h]
            if total >= h:
                return h
        