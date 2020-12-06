import math


def get_taken_seats(codes):
    max_f = []
    for code in codes:
        min_row, max_row, min_col, max_col, last_row, last_col = 0, 127, 0, 7, 0, 0
        for c in code:
            row_half = (min_row + max_row) / 2
            col_half = (min_col + max_col) / 2
            max_row = math.floor(row_half) if c == "F" else max_row
            min_row = math.ceil(row_half) if c == "B" else min_row
            last_row = min_row if c == "F" else last_row

            max_col = math.floor(col_half) if c == "L" else max_col
            min_col = math.ceil(col_half) if c == "R" else min_col
            last_col = min_col if c == "L" else max_col
        counted = (last_row * 8) + last_col
        max_f.append(counted)
    return max_f


def main():
    with open("5.txt", "r") as f:
        codes = [line.strip() for line in f.readlines()]
        taken_seats = get_taken_seats(codes)
        print(max(taken_seats))


main()
