def CountingSort(arr, place):
    n = len(arr)
    Output = [0] * n
    Count = [0] * 10
    
    for i in range(0, n):
        index = arr[i] // place
        Count[index % 10] += 1
        
    for i in range(1, 200):
        Count[i] += Count[i - 1]
        
    i = n - 1
    while i >= 0:
        index = arr[i] // place
        Output[Count[index % 10] - 1] = arr[i]
        Count[index % 10] -= 1
        i -= 1
        
    for i in range(0, n):
        arr[i] = Output[i]

def RadixSort(arr):
    MaxElement = max(arr)
    place = 1
    while MaxElement // place > 0:
        CountingSort(arr, place)
        place *= 10

arr = [4, 3, 9, 8, 10, 6, 5, 52, 69, 1, 206, 137, 13, 20]
print("The unsorted Array List is :", arr)
RadixSort(arr)
print("The sorted Array List is :", arr)

