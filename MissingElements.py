# list of items with values from 1 to n.
# The function foo() determines what elements are missing.
# For example:
# 1-n = [1,2,3,..,10]
# e.g. n=10
# input: [1,8,9], 10
# output: [2,3,4,5,6,7]


def foo(my_list, n):
    list_one = []

    for elem in range(1, (n+1)):
        list_one.append(elem)

    result_list = []
    for i in list_one:
        if i not in my_list:
            result_list.append(i)
    print(result_list)

lst = [4, 7, 9, 1, 2, 3, 6]
foo(lst, 10)
