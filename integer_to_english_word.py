class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        teens = {
            1: 'Eleven', 2: 'Twelve', 3: 'Thirteen', 4: 'Fourteen', 5: 'Fifteen',
            6: 'Sixteen', 7: 'Seventeen', 8: 'Eighteen', 9: 'Nineteen', 0: 'Ten'
        }
        dozen_to_str = {
            1: 'Ten', 2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty',
            6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'
        }
        unit_to_str = {
            1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'
        }
        ranks_to_str = {
            0: '', 1: ' Thousand', 2: ' Million', 3: ' Billion', 4: ' Trillion'
        }

        def before_1000(transforming):
            strs = []
            hundreds = transforming // 100
            if hundreds > 0:
                strs.append(
                    unit_to_str[hundreds] + ' Hundred'
                )
            transforming %= 100
            dozens = transforming // 10
            transforming %= 10
            units = transforming
            if dozens == 1:
                strs.append(
                    teens[units]
                )
            else:
                if dozens > 0:
                    strs.append(
                        dozen_to_str[dozens]
                    )
                if units > 0:
                    strs.append(
                        unit_to_str[units]
                    )
            return ' '.join(strs)
        digits = len(str(num))
        ranks = ceil(digits / 3)
        strs = deque()
        for rank in range(ranks):
            rank_num = num % 1000
            num //= 1000
            if rank_num > 0:
                strs.appendleft(
                    before_1000(rank_num) + ranks_to_str[rank]
                )
        return ' '.join(strs)
