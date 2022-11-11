matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(6)]
score = 0
for ball in range(3):

    row, col = [int(x) for x in input().strip('(').strip(')').split(', ')]

    if row < 0 or row >= 6 or col < 0 or col >= 6:
        continue
    elif matrix[row][col] == 'B':

        for i in range(6):
            for j in range(6):
                if j == col and matrix[i][j] != 'B':
                    score += matrix[i][j]
                    matrix[i][j] = 0
if 100 <= score <= 199:
    print(f"Good job! You scored {score} points, and you've won Football.")
elif 200 <= score <= 299:
    print(f"Good job! You scored {score} points, and you've won Teddy Bear.")
elif score >= 300:
    print(f"Good job! You scored {score} points, and you've won Lego Construction Set.")
else:
    print(f"Sorry! You need {100 - score} points more to win a prize.")
