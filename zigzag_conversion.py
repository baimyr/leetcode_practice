class Solution:
    def convert(self, s: str, numRows: int) -> str:
        numQty = len(s)
        nums_in_period = (numRows - 1) * 2 or 1
        periods = ceil(numQty / nums_in_period)
        to_mid = numRows - 1
        answer = ''
        rows = numRows - 1
        for row in range(numRows):
            reversed_row = rows - row
            for period in range(periods):
                start = period * nums_in_period
                if row == 0 or row == rows:
                    letter_id = start + row
                    answer += s[letter_id] if letter_id < numQty else ''
                    continue
                mid = start + to_mid
                before_mid_id = mid - reversed_row
                if before_mid_id < numQty:
                    answer += s[before_mid_id]
                after_mid_id = mid + reversed_row
                if after_mid_id < numQty:
                    answer += s[after_mid_id]
        return answer
