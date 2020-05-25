Is an in-place comparison based sorting algorithm based on the Binary Heap data structure(specifically the max heap, where parent node> child node). Heap sort is like selection sort, in that heap sort divides its input into a sorted and unsorted region, and it recursively shrinks the unsorted region by extracting the largest element from it and inserting into the sorted region. However unlike selection sort heap sort does not linearly scan the unsorted region, rather heap sort maintains the unsorted region in a max heap data structure to more quickly find the element in each step.

Space complexity: O(1) 

Time complexity; Worst case: O(nlog(n)) 

Average case: O(nlog(n)) 

Best case: O(nlog(n))

Data structure: Max Heap Tree.

If however data is in an array it first need to be converted to a Max Heap Tree. Steps Create max heap:

Remove the largest item(Root node). Place the item in a sorted partition array. This is done recursively of course
