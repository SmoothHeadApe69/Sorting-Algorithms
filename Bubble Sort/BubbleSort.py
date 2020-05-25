def BubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        if swapped == False:
            break

arr = [4, 3, 9, 8, 10, -6, 5, 52, 69, 1, 206, 137, 13, 20]

print("The unsorted Array List is :", arr)
BubbleSort(arr) #This calls the Bubble Sort function to run on arr AKA our Arrray List.

print("The sorted Array List is :" , arr)
