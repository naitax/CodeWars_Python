def flatten_and_sort(array):
    a = []
    for i in array:
        for j in i:
            a.append(j)
    a.sort()
    return a

print(flatten_and_sort([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]))
