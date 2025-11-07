class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1],reverse = True)
        n = len(boxTypes)
        i = 0
        units = 0
        remain = truckSize
        while i < n :
            box = boxTypes[i][0]
            unit = boxTypes[i][1]
            print(f'at i {i} box {box} and unit {unit}')
            # Take All boxes
            if box < remain:
                units += box * unit
                remain -= box
            # Remaining boxes
            elif remain > 0:
                units += remain * unit
                remain = 0
            print(f'remain {remain}')
            print(f'end of while units {units}')
            i += 1
        return units
