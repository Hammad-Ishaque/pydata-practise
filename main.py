# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)
f(2)
# output = [0, 1]
f(3,[3,2,1])
# output = [3, 2, 1, 0, 1, 4]
f(3)
# output = [0, 1, 4]


def get_new_list(n):
    new_list = [[0]]*n
    return new_list

if __name__ == '__main__':
    new_list = get_new_list(5)
    new_list[0][0] = 5
    # print(new_list)
    assert sum([i[0] for i in new_list]) == 5


def two_sum_optimize(arr):
    n = len(arr)


def two_sum(arr):
    target_element = arr[0]
    n = len(arr)
    output_list = []
    for i in range(1, n):
        for j in range(i + 1, n):
            sum_of_element = arr[i] + arr[j]
            if sum_of_element == target_element:
                result_str = str(arr[i]) + "," + str(arr[j])
                output_list.append(result_str)

    return ' '.join(output_list)


arr = [7, 3, 5, 2, -4, 8, 11]
print(two_sum(arr))