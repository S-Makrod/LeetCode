from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p,s in zip(position, speed)]
        cars.sort(key=lambda x: x[0])

        fleets = len(cars)
        bottleneck = cars[-1]

        for i in range(len(cars) - 2, -1, -1):
            t1 = (target - cars[i][0]) / cars[i][1]
            t2 = (target - bottleneck[0]) / bottleneck[1]

            if t1 <= t2:
                fleets -= 1
            else:
                bottleneck = cars[i]

        return fleets
