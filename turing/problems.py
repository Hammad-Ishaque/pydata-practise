# Find first duplicate from array
# First occurence of any element return this element
import sys


def first_duplicate(arr):
    duplicate_map = {}
    for i, v in enumerate(arr):
        if v in duplicate_map:
            return v
        duplicate_map[v] = 1
    return -1


def first_duplicate_without_space(arr):
    for i in range(0, len(arr)):
        if arr[abs(arr[i]) - 1] < 0:
            return abs(arr[i])
        else:
            arr[abs(arr[i]) - 1] = arr[abs(arr[i]) - 1] * -1


def print_triangle(n):
    for i in range(n):
        print('*' * (i + 1))


def first_non_repeating_character(word):
    character_mappper = {}
    first_index = len(word)
    for i, v in enumerate(word):
        if v not in character_mappper:
            first_index = i
            character_mappper[v] = 1
        else:
            character_mappper[v] += 1
    print(character_mappper)
    print(first_index)
    for k, v in character_mappper.items():
        if v == 1:
            return k
    return '_'


def fnr_without_map(word):
    char_counts = [0 for i in range(26)]
    for i, v in enumerate(word):
        char_counts[ord(v) - ord('a')] += 1
    for j, v in enumerate(word):
        if char_counts[ord(v) - ord('a')] == 1:
            return v
    return '_'


def max_profit(prices):
    min = sys.maxsize
    profit = 0
    for i, v in enumerate(prices):
        if v > min:
            profit = max(profit, v - min)
        else:
            min = v
    return profit


def get_product_except_self(arr):
    product = 1
    for i in arr:
        product *= i
    print(product)
    output = [product // i for i in arr]
    print(output)


def get_product_except_self_without_div(arr):
    product = 1
    left_product = [1 for i in range(len(arr))]
    right_product = [1 for i in range(len(arr))]
    output = []
    for j in range(1, len(arr)):
        left_product[j] = arr[j-1] * left_product[j-1]
    for i in range(len(arr)-2, -1, -1):
        right_product[i] = arr[i+1] * right_product[i+1]
    for i in range(0, len(arr)):
        output.append(left_product[i]*right_product[i])
    print(output)


# arr = [1, 2, 1, 2, 3, 3]
# arr = [2, 1, 3, 5, 3, 2]
# arr = [1, 2, 3, 4, 5, 6]
# print(first_duplicate(arr))
# print(first_duplicate_without_space(arr))
# print_triangle(5)
# str = "aaaacccceee"
# print(first_non_repeating_character(str))
# print(fnr_without_map(str))
# prices = [1, 2, 3, 4, 5]
# print(max_profit(prices))

arr = [1, 2, 3, 4]
# get_product_except_self(arr)
get_product_except_self_without_div(arr)
