from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = {}

        for val in hand:
            counts[val] = counts.get(val, 0) + 1

        vals = sorted(counts.keys())

        for val in vals:
            while counts[val] > 0:
                for key in range(val + 1, val + groupSize):
                    if key not in counts or counts[key] == 0:
                        return False
                    counts[key] -= 1
                counts[val] -= 1

        return True
