import sys

"""
Longest Increasing Subsequence using Dynamic Programming
"""


def lis(arr, i, n, prev):
    if i == n:
        return 0
    excl = lis(arr, i + 1, n, prev)
    incl = 0
    if arr[i] > prev:
        incl = 1 + lis(arr, i + 1, n, arr[i])
    return max(incl, excl)


"""
Maximum Sum Increasing Subsequence Problem
"""


def msis(arr, i, n, prev, sum):
    if i == n:
        return sum
    excl = msis(arr, i + 1, n, prev, sum)
    incl = sum
    if arr[i] > prev:
        incl = msis(arr, i, n, arr[i], sum + arr[i])
    return max(incl, excl)


def msis_btm(arr):
    sum_ = [0] * len(arr)
    sum_[0] = arr[0]
    for i in range(1, len(arr)):
        for j in range(i):
            if sum_[i] < sum_[j] and arr[i] > arr[j]:
                sum_[i] = sum_[j]
        sum_[i] += arr[i]
    return max(sum_)


def print_msis(arr):
    subsequence = [[] for _ in range(len(arr))]
    subsequence[0].append(arr[0])
    sum_ = [0] * len(arr)
    sum_[0] = arr[0]
    for i in range(1, len(arr)):
        for j in range(i):
            if sum_[i] < sum_[j] and arr[i] > arr[j]:
                subsequence[i] = subsequence[j].copy()
                sum_[i] = sum_[j]
        subsequence[i].append(arr[i])
        sum_[i] += arr[i]
    j = 0
    for i in range(1, len(arr)):
        if sum_[i] > sum_[j]:
            j = i
    return subsequence[j]


# Find minimum cost to reach the last cell of a matrix from its first cell
def min_cost_to_reach_last_cell(arr, m, n):
    if m == 0 or n == 0:
        return sys.maxsize
    if m == 1 or n == 1:
        return arr[0][0]
    return min(min_cost_to_reach_last_cell(arr, m - 1, n), min_cost_to_reach_last_cell(arr, m, n - 1)) \
           + arr[m - 1][n - 1]


# Find the size of the largest square submatrix of 1’s present in a binary matrix
def find_square_submatrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    T = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
    max_ = 0
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if matrix[i - 1][j - 1] == 1:
                T[i][j] = min(T[i][j - 1], T[i - 1][j - 1], T[i - 1][j]) + 1
                max_ = [max_, T[i][j]][T[i][j] > max_]
    return max_


if __name__ == '__main__':
    arr = [8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11]
    print(f'Longest increasing Subsequence() = {lis(arr, 0, len(arr), -sys.maxsize)}')
    print(f'Maximum Sum increasing Subsequence() = {msis(arr, 0, len(arr), -sys.maxsize, 0)}')
    print(f'Maximum Subsequence Btm() = {msis_btm(arr)}')
    print(f'Maximum Subsequence Print() = {print_msis(arr)}')
    cost = [
        [4, 7, 8, 6, 4],
        [6, 7, 3, 9, 2],
        [3, 8, 1, 2, 4],
        [7, 1, 7, 3, 7],
        [2, 9, 8, 9, 3]
    ]
    print(f'Find Minimum Cost To Reach Last Cell() = '
          f'{min_cost_to_reach_last_cell(cost, len(cost), len(cost[0]))}')
    # input matrix
    mat = [
        [0, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1]
    ]
    print(f'The size of largest square submatrix of 1s is() = {find_square_submatrix(mat)}')
