#Sorting algorithms are used to rearrange a given array or list of elements according to a comparison operator on the elements.
                                                     
                                                     Terminology:
                                                     
Divide & conquer: A divide-and-conquer algorithm works by breaking down a problem into smaller sub-problems of the same or related type, until they become simple enough to solve directly.

Comparison sorting: It involves elements in the given array list being compared to each by an operator mainly > or < operators that determines which of the two elements should occur first in the final sorted list.

In-place sorting: An in-place algorithm is an algorithm that does not need extra space and produces an output in the same memory that contains the data by transforming the input ‘in-place’. However, a small constant extra space used for variables is allowed.

Recursive algorithm: Is an algorithm which calls itself with "smaller (or simpler)" input values, and which obtains the result for the current input by applying simple operations to the returned value for the smaller (or simpler) input.

Stable algorithm: An algorithm is stable if two objects with equal keys appear in the same order in sorted output as they appear in the input unsorted array.

Space complexity: Refers to the memory space on your device used to solve the algorithm.

Time complexity: It’s the amount of time it takes to run the algorithm.

                                                    1. Bubble Sort:
                                                    

The bubble sort is a comparison-sort algorithm, which sorts items in an array by repeatedly stepping through the array, comparing adjacent elements and swaps them if they are in the incorrect order. The steps through the array are repeated until the array is sorted.

Space complexity: O(1)

Time complexity; Worst case: O (n^2)
            Average case: O(n^2)
            Best case: O(n)
Data structure: Array

                                                    2. Selection Sort:
                                                    

Is an in-place comparison sorting algorithm,which sorts a given array by repeatedly finding the minimum element from the unsorted part and putting it at the beginning. The algorithm maintains two sub-arrays at a given time.
The sub-array which is already sorted(Initially empty)
Remaining sub-array which is unsorted(Initially the entire input array)
Space complexity: O(1)
Time complexity; Worst case: O(n^2)
            Average case: O(n^2)
            Best case: O(n^2)
Data structure: Array
                                            
                                                   3. Insertion Sort
                                                    
                                                    
Is stable an in-place comparison sorting algorithm, which sorts an array by first dividing it into 2 seperate ‘sub-arrays’, where the first value of the array(since it doesn’t have items to its left), is considered sorted. We index up the array and compare the [n-1] and [n] indexed values and swap them if needed, if not proceed until the entire array is sorted.
Space complexity: O(1)
Time complexity; Worst case: O(n^2)
            Average case: O(n^2)
            Best case: O(n)
Data structure: Array

                                                     4. Merge Sort    
                                                     
                                                     
Is a stable divide & conquer algorithm, which divides the unsorted array list into sublists each containing 1 element. The resulting adjacent pairs of elements are compared and merged recursively until the list is fully sorted.
Space complexity: O(n)
Time complexity; Worst case: O(nlog(n))
            Average case: O(nlog(n))
            Best case: O(nlog(n))
Data structure: Array

                                                     5. Quick Sort
                                                     
                                                     
Is a divide and conquer, recursive algorithm which involves choosing a pivot from the given elements in an array and partitioning the other elements into 2 sub-arrays, such that all values less than the pivot are placed to its left and those greater than it are placed to the right. The sub-arrays are then sorted recursively until the entire array of items is sorted.
Space complexity: O(nlog(n))
Time complexity; Worst case: O(n^2)
            Average case: O(nlog(n))
            Best case: O(nlog(n))
Data structure: Array

                                                    6. Heap Sort
                                                    
                                                    
Is an in-place comparison based sorting algorithm based on the Binary Heap data structure(specifically the max heap, where parent  node> child node). Heap sort is like selection sort, in that heap sort divides its input into a sorted and unsorted region, and it recursively shrinks the unsorted region by extracting the largest element from it and inserting into the sorted region. However unlike selection sort heap sort does not linearly scan the unsorted region, rather heap sort maintains the unsorted region in a max heap data structure to more quickly find the element in each step.
Space complexity: O(1)
Time complexity; Worst case: O(nlog(n))
            Average case: O(nlog(n))
            Best case: O(nlog(n))
Data structure: Max Heap Tree. If however data is in an array it first need to be converted to a Max Heap Tree.
**Steps**
Create max heap.
Remove the largest item(Root node).
Place the item in a sorted partition array.
**This is done recursively of course**

                                                    7. Counting Sort
                                                    
Is a stable algorithm that sorts the elements of an array by counting the number of occurrences of each unique element in the array. The counts are stored in an auxiliary array and the sorting is done by mapping the counts as an index of the auxiliary array.
Space complexity: O(n+k), where k is the
Time complexity; Worst case: O(n+k)
            Average case: O(n+k)
Data structure: Array List                                                    
                                                    
                                                    
                                                   8. Radix Sort sort
                                                   
                                                   
Is an algorithm that sorts the elements by first grouping the individual digits of same place value **into a linked list**. It then sorts the elements according to their increasing or decreasing order. It is only used to sort numbers.
Space complexity: O(n+2)^2
Time complexity; Worst case: O(n * k/d)
            Average case: O(n * k/d)
            Best case : O(k(n+d))
Data structure: Array
 

                                                  9. Bucket sort
                                                 
                                                 
Is a comparison-sort based algorithm that sorts the elements into several groups called buckets. The elements inside each bucket are sorted using any of the other suitable sorting algorithms (mainly insertion sort, but it really depends on the average size of the buckets) recursively. Bucket sort is mainly used when input is uniformly distributed over a range.
Space complexity: O(n*k), where k is the number of buckets
Time complexity; Worst case: O(n^2)
            Average case: O(n + (n^2/k) + k ) , O(n) when k ≈ n
Data structure: Array List

                                                 10. Shell Sort
                                              
                                              
Is an in-place comparison sort, which first sorts the elements far apart from each other and successively reduces the interval between the elements to be sorted. It is a generalised version of the insert sort algorithm
In shell sort,elements at a specific interval are sorted . The interval between them is gradually decreased based on the sequence used. The performance of the shell sort depends on the type of sequence used in a given input array.
Shell’s original sequence: N/2 , N/4 , …, 1
Knuth’s increments: 1, 4, 13, …, (3k – 1) / 2
Sedgewick’s increments: 1, 8, 23, 77, 281, 1073, 4193, 16577...4j+1+ 3·2j+ 1.
Hibbard’s increments: 1, 3, 7, 15, 31, 63, 127, 255, 511…
Papernov & Stasevich increment: 1, 3, 5, 9, 17, 33, 65,...
Pratt: 1, 2, 3, 4, 6, 9, 8, 12, 18, 27, 16, 24, 36, 54, 81....
Space complexity: O(n)
Time complexity; Worst case: O(n^2)
            Average case: depends on the gap
Best case: O(nlog(n))
Data structure: Array List
                                  
