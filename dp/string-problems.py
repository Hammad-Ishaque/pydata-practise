"""Longest Common Subsequence Problem"""
import sys


def find_lcs_length(str1, str2, m, n, lookup={}):
    if m == 0 or n == 0:
        return 0
    key = (m, n)
    if key not in lookup:
        if str1[m - 1] == str2[n - 1]:
            lookup[key] = find_lcs_length(str1, str2, m - 1, n - 1) + 1
        else:
            lookup[key] = max(find_lcs_length(str1, str2, m - 1, n), find_lcs_length(str1, str2, m, n - 1))
    return lookup[key]


def find_lcs_length_btm(str1, str2):
    m, n = len(str1), len(str2)
    matr = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                matr[i][j] = matr[i - 1][j - 1] + 1
            else:
                matr[i][j] = max(matr[i - 1][j], matr[i][j - 1])
    return matr


def print_lcs(str1, str2, m, n, matr):
    if m == 0 or n == 0:
        return ""
    if str1[m - 1] == str2[n - 1]:
        return print_lcs(str1, str2, m - 1, n - 1, matr) + str1[m - 1]
    if matr[m - 1][n] > matr[m][n - 1]:
        return print_lcs(str1, str2, m - 1, n, matr)
    else:
        return print_lcs(str1, str2, m, n - 1, matr)


def print_all_lcs(str1, str2, m, n, matr):
    if m == 0 or n == 0:
        return [""]
    if str1[m - 1] == str2[n - 1]:
        lcs = print_all_lcs(str1, str2, m - 1, n - 1, matr)
        for i in range(len(lcs)):
            lcs[i] = lcs[i] + str1[m - 1]
        return lcs
    if matr[m - 1][n] > matr[m][n - 1]:
        return print_all_lcs(str1, str2, m - 1, n, matr)
    if matr[m][n - 1] > matr[m - 1][n]:
        return print_all_lcs(str1, str2, m, n - 1, matr)

    top = print_all_lcs(str1, str2, m - 1, n, matr)
    left = print_all_lcs(str1, str2, m, n - 1, matr)
    return top + left


"""
Longest common substring
"""


def find_lc_substring_length(str1, str2):
    m, n = len(str1), len(str2)
    max_length = 0
    ending_index = m
    lookup = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
                if lookup[i][j] > max_length:
                    max_length = lookup[i][j]
                    ending_index = i
    return str1[ending_index - max_length: ending_index]


"""
Longest palindromic subsequence
"""


def find_lps(str1, i, j, memo={}):
    if i > j:
        return 0
    if i == j:
        return 1
    key = (i, j)
    if key not in memo:
        if str1[i] == str1[j]:
            memo[key] = find_lps(str1, i + 1, j - 1) + 2
        else:
            memo[key] = max(find_lps(str1, i + 1, j), find_lps(str1, i, j - 1))
    return memo[key]


"""
Longest Repeated Subsequence Problem
"""


def find_lrs(str, m, n, memo={}):
    if m == 0 or n == 0:
        return 0
    key = (m, n)
    if key not in memo:
        if str[m - 1] == str[n - 1] and m != n:
            memo[key] = find_lrs(str, m - 1, n - 1) + 1
        else:
            memo[key] = max(find_lrs(str, m - 1, n), find_lrs(str, m, n - 1))
    return memo[key]


def find_lrs_btm(str, m):
    matr = [[0] * (m + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, m + 1):
            if str[i - 1] == str[j - 1] and i != j:
                matr[i][j] = matr[i - 1][j - 1] + 1
            else:
                matr[i][j] = max(matr[i - 1][j], matr[i][j - 1])
    return matr


def print_lrs(X, m, n, T):
    if m == 0 or n == 0:
        return ""
    if X[m - 1] == X[n - 1] and m != n:
        return print_lrs(X, m - 1, n - 1, T) + X[m - 1]
    else:
        if T[m - 1][n] > T[m][n - 1]:
            return print_lrs(X, m - 1, n, T)
        else:
            return print_lrs(X, m, n - 1, T)


"""
Implement Diff Utility
"""


def diff(X, Y, m, n, lookup):
    if m > 0 and n > 0 and X[m - 1] == Y[n - 1]:
        diff(X, Y, m - 1, n - 1, lookup)
        print("", X[m - 1], end='')
    elif n > 0 and (m == 0 or lookup[m][n - 1] >= lookup[m - 1][n]):
        diff(X, Y, m, n - 1, lookup)
        print(" +", Y[n - 1], end='')
    elif m > 0 and (n == 0 or lookup[m][n - 1] < lookup[m - 1][n]):
        diff(X, Y, m - 1, n, lookup)
        print(" -", X[m - 1], end='')


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


def wild_card_matching(str, pattern, m, n, lookup):
    if m < 0 and n < 0:
        return True
    elif m < 0:
        return False
    elif n < 0:
        for i in range(n + 1):
            if pattern[i] != '*':
                return False
        return True
    if not lookup[m][n]:
        if pattern[n] == "*":
            lookup[m][n] = wild_card_matching(str, pattern, m-1, n, lookup) or \
                           wild_card_matching(str, pattern, m, n - 1, lookup)
        else:
            if pattern[n] != "?" and pattern[n] != str[m]:
                lookup[m][n] = False
            else:
                lookup[m][n] = wild_card_matching(str, pattern, m-1, n-1, lookup)
    return lookup[m][n]


if __name__ == '__main__':
    X = "XMJYAUZ"
    Y = "MZJAWXU"
    max_length = find_lcs_length(X, Y, len(X), len(Y))
    print(max_length)
    matr = find_lcs_length_btm(X, Y)
    print(f'print lcs pair() = {print_lcs(X, Y, len(X), len(Y), matr)}')
    print(f'print all lcs pairs() = {print_all_lcs(X, Y, len(X), len(Y), matr)}')
    X = "ABC"
    Y = "BABA"
    print(f'Longest Common Substring() = {find_lc_substring_length(X, Y)}')
    X = "ABBDCACB"
    print(f'Longest Palindromic Subsequence() = {find_lps(X, 0, len(X) - 1)}')
    print(f'Palindrome Strings() = '
          f'{print_lcs(X, X[::-1], len(X), len(X), find_lcs_length_btm(X, X[::-1]))}')
    X = "ATACTCGGA"
    m = len(X)
    print(f'Longest Repeating Subsequence() = {find_lrs(X, m, m)}')
    # print(f'Longest Repeating Sequence Btm() = {find_lrs_btm(X, m)}')
    print(f'Longest Repeating Print()= {print_lrs(X, m, m, find_lrs_btm(X, m))}')
    X = "ABCDFGHJQZ"
    Y = "ABCDEFGIJKRXYZ"
    print("Diff Utility() = ", end='')
    diff(X, Y, len(X), len(Y), find_lcs_length_btm(X, Y))
    # print(f'Diff Utility() = {diff(X, Y, len(X), len(Y), find_lcs_length_btm(X, Y))}')
    arr = [8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11]
    print()
    print(f'Maximum Sum increasing Subsequence() = {msis(arr, 0, len(arr), -sys.maxsize, 0)}')
    print(f'Maximum Subsequence Btm() = {msis_btm(arr)}')
    print(f'Maximum Subsequence Print() = {print_msis(arr)}')
    str = "xyxzzxy"
    pattern = "x***x?"
    m = len(str)
    n = len(pattern)
    lookup = [[0]*(n+1) for _ in range(m+1)]
    print(f'Wild Card Matching String() = '
          f'{wild_card_matching(str, pattern, m-1, n-1, lookup)}')
