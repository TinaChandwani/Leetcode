class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        commonDict = defaultdict(int)
        minSum = float('inf')
        output = []
        for i in range(len(list1)):
            commonDict[list1[i]] = i 

        for i in range(len(list2)):
            if list2[i] in commonDict:
                minIndex = i + commonDict[list2[i]]
                if minIndex < minSum:
                    minSum = minIndex
                    output =[]
                    output.append(list2[i])
                elif minIndex == minSum:
                    output.append(list2[i])
        return output