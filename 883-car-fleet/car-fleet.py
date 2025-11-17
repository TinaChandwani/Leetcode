class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        Basically the point is to sort the cars using positions
        '''
        cars = sorted(zip(position,speed), key = lambda x:x[0])
        print(f'cars {cars}')
        stack = []
        n = len(cars)
        arrival = []
        for i in cars:
            p = i[0]
            s = i[1]
            arr_time = (abs((target - p) / s))
            arrival.append(arr_time)
        
        print(f'arrival {arrival}')
        
        for j in range(n-1,-1,-1):
            t = arrival[j]
            if not stack or t > stack[-1]:
                stack.append(t)
        return len(stack)