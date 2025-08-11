class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # BFS Technique
        # basically every word is a node and the next mututaion is the next node in the graph
        # This problem is basically => To calculate shortest distance between two nodes in a graph which naturally BFS does

        bank = set(bank)
        if endGene not in bank:
            return -1
        if endGene == startGene:
            return 0
        
        q = deque()
        visit = set(startGene)
        q.append([startGene,0]) # [gene, no of mutations]
        
        while q:
            # Pop the queue
            gene,m = q.popleft()
            if gene == endGene:
                return m
            # calculate next gene
            for i in range(len(gene)):
                for letter in "ACTG":
                    new_gene = gene[:i] + letter + gene[i+1:]
                    if new_gene in bank and new_gene not in visit :
                        q.append([new_gene,m+1])
                        visit.add(new_gene)
        return -1