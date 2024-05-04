<h1>index</h1>

<br/>

<ol>
<li><a href="">Selection Sort</a></li>
<li><a href="">Bubble Sort</a></li>
<li><a href="">Recursive Bubble Sort</a></li>
<li><a href="">Insertion Sort</a></li>
<li><a href="">Recursive Insertion Sort</a></li>
<li><a href="">Merge Sort</a></li>
<li><a href="">Iterative Merge Sort</a></li>
<li><a href="">Quick Sort</a></li>
<li><a href="">Iterative Quick Sort</a></li>
<li><a href="">Heap Sort</a></li>
<li><a href="">Counting Sort</a></li>
<li><a href="">Radix Sort</a></li>
<li><a href="">Bucket Sort</a></li>
<li><a href="">ShellSort</a></li>
<li><a href="">TimSort</a></li>
<li><a href="">Comb Sort</a></li>
<li><a href="">Pigeonhole Sort</a></li>
<li><a href="">Cycle Sort</a></li>
<li><a href="">Cocktail Sort</a></li>
<li><a href="">Strand Sort</a></li>
<li><a href="">Bitonic Sort</a></li>
<li><a href="">Pancake sorting</a></li>
<li><a href="">Binary Insertion Sort</a></li>
<li><a href="">BogoSort or Permutation Sort</a></li>
<li><a href="">Gnome Sort</a></li>
<li><a href="">Sleep Sort – The King of Laziness / Sorting while Sleeping</a></li>
<li><a href="">Structure Sorting (By Multiple Rules) </a></li>
<li><a href="">Stooge Sort</a></li>
<li><a href="">Tag Sort (To get both sorted and original)</a></li>
<li><a href="">Tree Sort</a></li>
<li><a href="">Cartesian Tree Sorting</a></li>
<li><a href="">Odd-Even Sort / Brick Sort</a></li>
<li><a href="">QuickSort on Singly Linked List</a></li>
<li><a href="">QuickSort on Doubly Linked List</a></li>
<li><a href="">3-Way QuickSort (Dutch National Flag)</a></li>
<li><a href="">Merge Sort for Linked Lists</a></li>
<li><a href="">Merge Sort for Doubly Linked List</a></li>
<li><a href="">3-way Merge Sort</a></li>
</ol>

***

<h2>Selection sort</h2>

**Selection sort**, algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from the unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
<ol>
<li> The subarray which is already sorted.</li>
<li> Remaining subarray which is unsorted.</li>

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

#### Properties:
- Worst-case performance O(n^2)
- Best-case performance O(n)
- Average case performance O(n^2)

**read more at: [Wikipedia](https://en.wikipedia.org/wiki/Selection_sort)**<br>
**code: [Selection sort](https://github.com/TheAlgorithms/Python/blob/master/sorts/selection_sort.py)**

***


<h2>Bubble sort</h2>

**Bubble sort**, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. The algorithm, which is a comparison sort, is named for the way smaller elements "bubble" to the top of the list. Although the algorithm is simple, it is too slow and impractical for most problems even when compared to insertion sort. It can be practical if the input is usually in sorted order but may occasionally have some out-of-order elements nearly in position.

#### Properties:
- Worst-case performance O(n^2)
- Best-case performance O(n)
- Average case performance O(n^2)

**read more at: [Wikipedia](https://en.wikipedia.org/wiki/Bubble_sort)**<br>
**code: [Bubble sort](https://github.com/TheAlgorithms/Python/blob/master/sorts/bubble_sort.py)**

***


<h2>Insertion sort</h2>

**Insertion sort** is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

#### Properties:
- Worst-case performance O(n^2)
- Best-case performance O(n)
- Average case performance O(n^2)

**read more at: [Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort)**<br>
**code: [Insertion sort](https://github.com/TheAlgorithms/Python/blob/master/sorts/insertion_sort.py)**
