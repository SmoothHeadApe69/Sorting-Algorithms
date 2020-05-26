Is an in-place comparison sort, which first sorts the elements far apart from each other and successively reduces the interval between the elements to be sorted. 
It is a generalised version of the insert sort algorithm In shell sort,elements at a specific interval are sorted . 
The interval between them is gradually decreased based on the sequence used. 
The performance of the shell sort depends on the type of sequence used in a given input array. 
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
