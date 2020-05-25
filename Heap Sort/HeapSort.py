def Heapify(arr, n, i):
  largest = i
  l = 2*i + 1
  r = 2*i + 2

  if l < n and arr[i] < arr[l]:
    largest = l

  if r < n and arr[largest] < arr[r]:
    largest = r

  #Changeing the root if needed
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]

    #Heapifying the root 
    Heapify(arr, n, largest)

def HeapSort(arr):
  n = len(arr)

  for i in range(n, -1, -1):
    Heapify(arr, n, i)

  for i in range(n-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    Heapify(arr, i, 0)

arr = [4, 3, 9, 8, 10, -6, 5, 52, 69, 1, 206, 137, 13, 20]
print("The unsorted Array List is :", arr)
HeapSort(arr) #This calls the Heap Sort function to run on arr AKA our Arrray List.
n = len(arr)
HeapSort(arr)
print("The sorted Array List is :" , arr)
