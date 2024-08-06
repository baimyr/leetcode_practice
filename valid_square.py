class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        ps = [p1, p2, p3, p4]
        ps.sort()
        first = ps[0]
        second = ps[1]
        third = ps[2]
        fourth = ps[3]
        return (second[0] - first[0]) ** 2 + (second[1] - first[1]) ** 2 == (third[0] - first[0]) ** 2 + (third[1] - first[1]) ** 2 == (second[0] - fourth[0]) ** 2 + (second[1] - fourth[1]) ** 2 == (third[0] - fourth[0]) ** 2 + (third[1] - fourth[1]) ** 2 != 0 and (fourth[0] - first[0]) ** 2 + (fourth[1] - first[1]) ** 2 == (second[0] - third[0]) ** 2 + (second[1] - third[1]) ** 2
