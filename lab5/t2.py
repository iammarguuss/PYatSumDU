n = 7

array = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        array[i][j] = j - i + 1

for row in array:
    print(' '.join(map(str, row)))
