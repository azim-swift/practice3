# С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, 
# B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное.

# Вариант 7
# Формируется матрица F следующим образом: если в С количество нулевых элементов в нечетных столбцах в области 4 больше, 
# чем количество нулевых  элементов в четных столбцах в области 1, то поменять в В симметрично области 2 и 3 местами, иначе С и Е поменять местами несимметрично. 
# При этом матрица А не меняется. После чего вычисляется выражение: ((F*A)– (K * AT) . Выводятся по мере формирования А, F и все матричные операции последовательно.


import random

def generate_matrix(N):
    matrix = []
    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(random.randint(-10, 10))
        matrix.append(row)
    return matrix

def count_zeros(matrix, region):
    count = 0
    for i in range(region[0], region[1]):
        for j in range(region[2], region[3]):
            if matrix[i][j] == 0:
                count += 1
    return count

def swap_regions(matrix, region1, region2):
    for i in range(region1[0], region1[1]):
        for j in range(region1[2], region1[3]):
            temp = matrix[i][j]
            matrix[i][j] = matrix[region2[0]+i-region1[0]][region2[2]+j-region1[2]]
            matrix[region2[0]+i-region1[0]][region2[2]+j-region1[2]] = temp

def transpose_matrix(matrix):
    N = len(matrix)
    for i in range(N):
        for j in range(i+1, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def compute_expression(A, F, K):
    N = len(A)
    AT = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            AT[i][j] = A[j][i]

    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += F[i][k] * A[k][j]
            result[i][j] -= K * AT[i][j]

    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Ввод размерности матрицы и значения K
N = int(input("Введите размерность матрицы: "))
K = int(input("Введите значение K: "))

# Генерация случайной матрицы A
A = generate_matrix(N)
print("Матрица A:")
print_matrix(A)

# Формирование подматриц B, C, D, E целенаправленно
B = [[1] * (N // 2) for _ in range(N // 2)]
C = [[2] * (N // 2) for _ in range(N // 2)]
D = [[3] * (N // 2) for _ in range(N // 2)]
E = [[4] * (N // 2) for _ in range(N // 2)]

# Формирование матрицы F в соответствии с условием задачи
region1 = (0, N // 2, 0, N // 2)
region2 = (0, N // 2, N // 2, N)
if count_zeros(C, region2) > count_zeros(C, region1):
    swap_regions(B, region2, region1)
else:
    swap_regions(C, region2, region1)

F = B + C + D + E
print("Матрица F:")
print_matrix(F)

# Вычисление выражения ((F*A) - (K * AT))
result = compute_expression(A, F, K)
print("Результат вычисления выражения:")
print_matrix(result)
