def Partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    
    for j in range(low, high):
        if arr[j] < pivot:
            i+= 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return(i + 1)

def QuickSort(arr, low, high):
    if low < high:
        pi = Partition(arr, low, high)
        
        QuickSort(arr, low,pi - 1)
        QuickSort(arr, pi + 1, high)

arr = [4, 3, 9, 8, 10, -6, 5, 52, 69, 1, 206, 137, 13, 20]
n = len(arr)
print("The unsorted Array List is :", arr)
QuickSort(arr, 0, n-1) #This calls the Quick Sort function to run on arr AKA our Arrray List.
print("The sorted Array List is :" , arr)

