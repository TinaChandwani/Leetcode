class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        If the len of hand is not divisible by the groupSize -> it is possible to 
        break down into groups

        '''
        n = len(hand)
        if n % groupSize != 0 :
            return False
        sDict = defaultdict(int)
        hand.sort()

        for i in hand:
            sDict[i] += 1


        for s in range(n):
            small = hand[s]
            if sDict[small] > 0:
                # We need to find the group
                for _ in range(groupSize):
                    next_ele = small + _
                    if next_ele not in sDict:
                        return False
                    else:
                        sDict[next_ele] -= 1
                    if sDict[next_ele] == 0:
                        del sDict[next_ele]
        return True

        