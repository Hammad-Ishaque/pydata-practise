arr = [7, 3, 5, 2, -4, 8, 11]

def two_sum(arr):
    arr1 = arr[1:]
    arr1.sort()
    print(arr1)
    i, j = 0, len(arr1)-1
    while i < j:
        if arr1[i] + arr1[j] == arr[0]:
            print(arr1[i], arr1[j])
            i += 1
            j -= 1
        elif arr1[i] + arr1[j] < arr[0]:
            i += 1
        else:
            j -= 1


def max_product(arr):
    curr_prod = 1
    max_prod = 1
    for i in arr:
        if i != max(arr):
            curr_prod = max(curr_prod, max(arr) * i)
            max_prod = max(curr_prod, max_prod)
    print(curr_prod, max_prod)


def find_middle_node(arr):
    i, j = 0, len(arr)-1
    while i <= j:
        if j-i == 1:
            print(arr[i], arr[j])
        elif i == j:
            print(arr[i])
        i += 1
        j -= 1

two_sum(arr)
arr = [2, 4, 7, 1, 3, 5, 7]
# max_product(arr)
print(arr)
find_middle_node(arr)