# С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, 
# B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное.

# Вариант 7
# Формируется матрица F следующим образом: если в С количество нулевых элементов в нечетных столбцах в области 4 больше, 
# чем количество нулевых  элементов в четных столбцах в области 1, то поменять в В симметрично области 2 и 3 местами, иначе С и Е поменять местами несимметрично. 
# При этом матрица А не меняется. После чего вычисляется выражение: ((F*A)– (K * AT) . Выводятся по мере формирования А, F и все матричные операции последовательно.

import random

def swap_areas(matrix1, matrix2):
    temp = matrix1.copy()
    matrix1 = matrix2.copy()
    matrix2 = temp
    return matrix1, matrix2

def calculate_expression(K, N):
    # Случайным образом заполнение матрицы А [-10, 10]
    A = [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]

    # Заполнение подматрицы с интервалом [-10, 10]
    D = [[random.randint(-10, 10) for _ in range(N // 2)] for _ in range(N // 2)]
    E = [[random.randint(-10, 10) for _ in range(N // 2)] for _ in range(N // 2)]
    C = [[random.randint(-10, 10) for _ in range(N // 2)] for _ in range(N // 2)]
    B = [[random.randint(-10, 10) for _ in range(N // 2)] for _ in range(N // 2)]


    # Проверка на состояние и при необходимсоти замена местами
    if sum(C[i][j] != 0 for i in range(1, N // 2, 2) for j in range(2)) > sum(C[i][j] != 0 for i in range(0, N // 2, 2) for j in range(N // 2 - 2, N // 2)):
        B = swap_areas(B, B)  # Swap areas 2 and 3 in B
    else:
        C, E = swap_areas(C, E)  # Swap C and E

    # Вычесление матрицы
    F = [[0] * N for _ in range(N)]
    for i in range(N // 2):
        for j in range(N // 2):
            F[i][j] = B[i][j]
            F[i][j + N // 2] = C[i][j]
            F[i + N // 2][j] = D[i][j]
            F[i + N // 2][j + N // 2] = E[i][j]

    # Вычесление выражения ((F * A) - (K * A transpose))
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = sum(F[i][k] * A[k][j] for k in range(N)) - K * A[j][i]

    # Вывод матрицы с результатом
    print("Матрица A:")
    for row in A:
        print(row)
    print("Матрица F:")
    for row in F:
        print(row)
    print("Вывод:")
    for row in result:
        print(row)

# Тест самой программы
K = int(input("Введите K: "))
N = int(input("Ввелите N: "))
calculate_expression(K, N)
