class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        height_len = len(height)
        finish = height_len - 1
        distance = height_len - 1
        max_area = min(height[start], height[finish]) * distance
        for _ in range(height_len):
            start_height = height[start]
            finish_height = height[finish]
            if start_height < finish_height:
                max_area = max(start_height * distance, max_area)
                start += 1
                distance -= 1
            else:
                max_area = max(finish_height * distance, max_area)
                finish -= 1
                distance -= 1
        return max_area
