def CountingSort(arr):
    n = len(arr)
    Output = [0] * n
    Count = [0] * 10

    for i in range(0, n):
        Count[arr[i]] += 1

    for i in range(-100, 200):
        Count[i] += Count[i - 1]

    i = n - 1
    while i >= 0:
        Output[Count[arr[i]] - 1 ] = arr[i]
        Count[arr[i]] -= 1
        i -= 1
    
    for i in range(0, n):
        arr[i] = Output[i]

arr = [4, 3, 9, 8, 10, -6, 5, 52, 69, 1, 206, 137, 13, 20]
print("The unsorted Array List is :", arr)
CountingSort(arr)
print("The sorted Array List is :", arr)

