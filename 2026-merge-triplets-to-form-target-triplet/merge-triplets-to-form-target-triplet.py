class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        '''
        you can ignore any triplet that has a value exceeding the target in any position.
        Filter out any triplet that exceeds the target in any position
        Merge all remaining triplets and check if the result equals the target      
        '''
        t1,t2,t3 = target[0],target[1],target[2]
        a1,b1,c1 = 0,0,0
        for i in triplets:
            a,b,c = i[0],i[1],i[2]
            if a > t1 or b > t2 or c > t3:
                continue
            else:
                a1,b1,c1 = max(a1,a),max(b1,b),max(c1,c) # 1 3 4
            if a1 == t1 and b1 == t2 and c1 == t3:
                return True
        return False


        