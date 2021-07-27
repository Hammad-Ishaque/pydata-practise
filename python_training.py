def test(nums):
    for i in nums:
        if i == 0:  # if the condition is satisfied, it hits break and the else block will not run
            print('There is a 0.')
            break
    else:
        print('There are no 0s.')


test([1, 2, 3, 0])  # There is a 0.
test([1, 2, 3])  # There are no 0s.