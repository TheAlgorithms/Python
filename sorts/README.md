


## There are a lot of algorithms used for sorting things:

- [Bubble Sort](#bubble-sort)
- [Insertion Sort](#insertion-sort)
- [Merge Sort](#merge-sort)
- [Quick Sort](#quick-sort)
- [Selection Sort](#selection-sort)
- [Shell Sort](#shell-sort)

[Here](sorting-graphs.png) are some graphs comparing time complexity of these sorting algorithms.

### Bubble Sort
![alt text][bubble-image]

[Bubble sort][bubble-wiki], sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

__Properties__
* Worst case performance	`O(n^2)`
* Best case performance	`O(n)`
* Average case performance	`O(n^2)`

###### View the algorithm in [action][bubble-toptal]



### Insertion Sort
![alt text][insertion-image]

[Insertion sort][insertion-wiki] is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

__Properties__
* Worst case performance	`O(n^2)`
* Best case performance	`O(n)`
* Average case performance	`O(n^2)`

###### View the algorithm in [action][insertion-toptal]


### Merge Sort
![alt text][merge-image]

[Mergesort][merge-wiki] is a divide and conquer algorithm that was invented by John von Neumann in 1945. It is an efficient, general-purpose, comparison-based sorting algorithm. Most implementations produce a stable sort, which means that the implementation preserves the input order of equal elements in the sorted output. 

__Properties__
* Worst case performance `O(n log n)`
* Best case performance	`O(n)`
* Average case performance	`O(n)`


###### View the algorithm in [action][merge-toptal]

### Quick Sort
![alt text][quick-image]

[Quicksort][quick-wiki] (sometimes called partition-exchange sort) is an efficient sorting algorithm, serving as a systematic method for placing the elements of an array in order.
It works by choosing a pivot element and finding it's right position in the array by rearranging elements.

__Properties__
* Worst case performance	`O(n^2)`
* Best case performance	`O(n log n)` or `O(n)` with three-way partition
* Average case performance	`O(n log n)`

###### View the algorithm in [action][quick-toptal]

### Selection Sort
![alt text][selection-image]

[Selection Sort][selection-wiki] divides the input list into two parts: the sublist of items already sorted, which is built up from left to right at the front (left) of the list, and the sublist of items remaining to be sorted that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.

__Properties__
* Worst case performance	`O(n^2)`
* Best case performance	`O(n^2)`
* Average case performance	`O(n^2)`

###### View the algorithm in [action][selection-toptal]

### Shell Sort
![alt text][shell-image]

[Shellsort][shell-wiki] is a generalization of insertion sort that allows the exchange of items that are far apart.  The idea is to arrange the list of elements so that, starting anywhere, considering every nth element gives a sorted list.  Such a list is said to be h-sorted.  Equivalently, it can be thought of as h interleaved lists, each individually sorted.

__Properties__
* Worst case performance `O(nlog2 2n)`
* Best case performance `O(n log n)`
* Average case performance depends on gap sequence

###### View the algorithm in [action][shell-toptal]


[bubble-toptal]: https://www.toptal.com/developers/sorting-algorithms/bubble-sort
[bubble-wiki]: https://en.wikipedia.org/wiki/Bubble_sort
[bubble-image]: https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Bubblesort-edited-color.svg/220px-Bubblesort-edited-color.svg.png "Bubble Sort"

[insertion-toptal]: https://www.toptal.com/developers/sorting-algorithms/insertion-sort
[insertion-wiki]: https://en.wikipedia.org/wiki/Insertion_sort
[insertion-image]: https://upload.wikimedia.org/wikipedia/commons/7/7e/Insertionsort-edited.png "Insertion Sort"

[quick-toptal]: https://www.toptal.com/developers/sorting-algorithms/quick-sort
[quick-wiki]: https://en.wikipedia.org/wiki/Quicksort
[quick-image]: https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif "Quick Sort"

[merge-toptal]: https://www.toptal.com/developers/sorting-algorithms/merge-sort
[merge-wiki]: https://en.wikipedia.org/wiki/Merge_sort
[merge-image]: https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif "Merge Sort"

[selection-toptal]: https://www.toptal.com/developers/sorting-algorithms/selection-sort
[selection-wiki]: https://en.wikipedia.org/wiki/Selection_sort
[selection-image]: https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Selection_sort_animation.gif/250px-Selection_sort_animation.gif "Selection Sort Sort"

[shell-toptal]: https://www.toptal.com/developers/sorting-algorithms/shell-sort
[shell-wiki]: https://en.wikipedia.org/wiki/Shellsort
[shell-image]: https://upload.wikimedia.org/wikipedia/commons/d/d8/Sorting_shellsort_anim.gif "Shell Sort"
