class BookMyShow:

    def __init__(self, n: int, m: int):
        self.rows = n
        self.seats = m 
        self.available_seats = {}
        self.bottom = 0
        self.gather_bottom_for_values = {}
        self.available_seats_count = n * m

    def gather(self, k: int, maxRow: int) -> List[int]:
        current_bottom = self.gather_bottom_for_values.get(k, self.bottom)
        if k > self.seats:
            return []
        for row_number in range(current_bottom, maxRow + 1):
            available_seat = self.available_seats.get(row_number, 0)
            if available_seat is None or available_seat + k > self.seats:
                continue
            available_seat_updated = available_seat + k
            if available_seat_updated == self.seats:
                self.available_seats[row_number] = None
                if self.bottom == row_number:
                    self.bottom = row_number
            else:
                self.available_seats[row_number] = available_seat_updated
                self.gather_bottom_for_values[k] = row_number
            self.available_seats_count -= k
            return [row_number, available_seat]
        return []

    def scatter(self, k: int, maxRow: int) -> bool:
        sat = 0
        occupied_rows = []
        if k > (maxRow + 1) * self.seats or k > self.available_seats_count:
            return False
        for row_number in range(self.bottom, maxRow + 1):
            available_seat = self.available_seats.get(row_number, 0)
            if available_seat is None:
                continue

            seats_in_row = self.seats - available_seat
            sat_in_row = min(k - sat, seats_in_row)
            sat += sat_in_row
            new_available_seat = available_seat + sat_in_row
            if new_available_seat >= self.seats:
                occupied_rows.append(row_number)
            else:
                self.available_seats[row_number] = new_available_seat
            if sat == k:
                new_rows_values = dict.fromkeys(occupied_rows)
                if occupied_rows and self.bottom == occupied_rows[0]:
                    self.bottom = occupied_rows[-1] + 1
                self.available_seats.update(new_rows_values)
                self.available_seats_count -= k
                return True
        return False

# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)