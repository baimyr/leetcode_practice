class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combinations(res: List[int], s: List[int], a: deque, nested_level: int):
            for _ in range(len(a)):
                number = a.popleft()
                if nested_level == k:
                    res.append(s + [number])
                else:
                    combinations(res, s + [number], a.copy(), nested_level + 1)
        res = []
        combinations(res, [], deque(range(1, n + 1)), 1)
        return res
