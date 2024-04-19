# С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, 
# B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное.

# Вариант 7
# Формируется матрица F следующим образом: если в С количество нулевых элементов в нечетных столбцах в области 4 больше, 
# чем количество нулевых  элементов в четных столбцах в области 1, то поменять в В симметрично области 2 и 3 местами, иначе С и Е поменять местами несимметрично. 
# При этом матрица А не меняется. После чего вычисляется выражение: ((F*A)– (K * AT) . Выводятся по мере формирования А, F и все матричные операции последовательно.

import random

def count_zeros(matrix, start_row, end_row, start_col, end_col):
    if not matrix:  # Проверка на пустую матрицу
        return 0
    zeros_count = 0
    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            if i >= len(matrix) or j >= len(matrix[0]):  # Проверка на выход за границы матрицы
                continue
            if matrix[i][j] == 0:
                zeros_count += 1
    return zeros_count
def swap_regions(matrix, region1, region2):
    temp = matrix[region1[0]:region1[1], region1[2]:region1[3]].copy()
    matrix[region1[0]:region1[1], region1[2]:region1[3]] = matrix[region2[0]:region2[1], region2[2]:region2[3]]
    matrix[region2[0]:region2[1], region2[2]:region2[3]] = temp
def generate_matrix(N, K):
    if K > N // 2:  # Проверка на допустимый размер K
        raise ValueError("K must be less than or equal to half the size of the matrix N.")
    A = [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]
    print("Матрица A:")
    print_matrix(A)
    return A
def form_matrix_F(A, K):
    B = A[:K]
    C = A[:K][K:]
    D = A[K:][:K]
    E = A[K:][K:]
    region1 = [0, K, K, 2 * K]
    region2 = [K, 2 * K, 0, K]
    zeros_odd_cols_region4 = count_zeros(C, 0, K, K, 2 * K)
    zeros_even_cols_region1 = count_zeros(C, 0, K, 0, K)

    if zeros_odd_cols_region4 > zeros_even_cols_region1:
        swap_regions(B, region1, region2)
    else:
        temp = C.copy()
        C = E.copy()
        E = temp.copy()
    F = [[*row] for row in B] + [[*row] for row in C] + [[*row] for row in D] + [[*row] for row in E]
    print("Матрица F:")
    print_matrix(F)
    return F
def calculate_expression(F, A, K):
    FA = multiply_matrices(F, A)
    AT = transpose_matrix(A)
    KAT = multiply_matrix_by_scalar(K, AT)
    result = subtract_matrices(FA, KAT)
    print("Результат вычисления выражения ((F * A) - (K * AT)):")
    print_matrix(result)
def print_matrix(matrix):
    for row in matrix:
        print(row)
def multiply_matrices(A, B):
    result = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    return result
def transpose_matrix(A):

    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
def multiply_matrix_by_scalar(k, A):
   return [[k * element for element in row] for row in A]
def subtract_matrices(A, B):
    return [[a - b for a, b in zip(A_row, B_row)] for A_row, B_row in zip(A, B)]

N = int(input("Введите размер матрицы N: "))
K = int(input("Введите размер подматрицы K: "))
A = generate_matrix(N, K)
F = form_matrix_F(A, K)

calculate_expression(F, A, K)
