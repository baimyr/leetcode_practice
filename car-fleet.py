class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        rt = (0, float("-inf"))
        for position, speed in reversed(sorted(list(zip(position, speed)), key=lambda x: x[0])):
            if (target - position) / speed > rt[1]: rt = (rt[0] + 1, (target - position) / speed,)
        return rt[0]
