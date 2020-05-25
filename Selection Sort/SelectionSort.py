def SelectionSort(arr):
    n = len(arr)
    
    for i in range (n - 1):
        min_index = i
        
        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [4, 3, 9, 8, 10, -6, 5, 52, 69, 1, 206, 137, 13, 20]

print("The unsorted Array List is :", arr)
SelectionSort(arr) #This calls the Selection Sort function to run on arr AKA our Arrray List.

print("The sorted Array List is :" , arr)
