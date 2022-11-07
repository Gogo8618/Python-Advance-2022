def knight_finder(desk_, row_, col_):
    move = [[row_ + 2, col_ + 1],
            [row_ + 2, col_ - 1],
            [row_ - 2, col_ + 1],
            [row_ - 2, col_ - 1],
            [row_ + 1, col_ + 2],
            [row_ + 1, col_ - 2],
            [row_ - 1, col_ + 2],
            [row_ - 1, col_ - 2]]

    result = 0
    for r, c in move:
        if 0 <= r < len(desk_) and 0 <= c < len(desk_) and desk_[r][c] == 'K':
            result += 1
    return result


size = int(input())

desk = []
removed_knight = 0
for _ in range(size):
    desk.append(list(input()))

while True:
    best_knight = 0
    knight_row = 0
    knight_col = 0
    for row in range(size):
        for col in range(size):
            if desk[row][col] == '0':
                continue
            count = knight_finder(desk, row, col)
            if count > best_knight:
                best_knight = count
                knight_row = row
                knight_col = col
    if best_knight == 0:
        break
    desk[knight_row][knight_col] = '0'
    removed_knight += 1
print(removed_knight)
