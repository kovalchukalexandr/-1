n, m = map(int, input("Введите размеры массива n и m: ").split())

def fill_snake_array(n, m):
    A = [[0] * m for _ in range(n)]
    num = 1
    for j in range(m):
        if j % 2 == 0:
            for i in range(n):
                A[i][j] = num
                num += 1
        else:
            for i in range(n - 1, -1, -1):
                A[i][j] = num
                num += 1
    return A
def print_array(arr):
    for row in arr:
        print(' '.join(map(str, row)))



snake_array = fill_snake_array(n, m)
print_array(snake_array)


