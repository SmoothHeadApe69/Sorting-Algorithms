def ShellSort(arr):
    n = len(arr)
    Gap = n // 2
    
    while Gap > 0:
        for i in range(Gap, n):
            temp = arr[i]
            
            j=i
            while j > Gap and arr[j - Gap] > temp:
                arr[j] = arr[j - Gap]
                j -= Gap
            arr[j] = temp
            
        Gap //= 2
        
arr = [4, 3, 9, 8, 10, 6, 5, 52, 69, 1, 206, 137, 13, 20]
print("The unsorted Array List is :", arr)
ShellSort(arr)
print("The sorted Array List is :", arr)
