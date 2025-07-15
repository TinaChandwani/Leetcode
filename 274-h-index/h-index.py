class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        U -> n cannot be a negative integer
        M -> 
        I ->
        1) Sort the array in decending order
        2) check if citations[i] >= i + 1 (array is 0 indexed)
        3) update hindex accordlingly 
        """

        citations.sort(reverse = True)
        n = len(citations)
        h_index = 0

        for i in range(n):
            if citations[i] >= i + 1:
                h_index = i + 1
            else:
                break
        return h_index