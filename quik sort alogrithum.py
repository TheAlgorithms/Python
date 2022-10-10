quickSort(arr[], low, high) {

  // Till starting index is lesser than ending index
  if (low < high) {

    // pi is partitioning index,
    // arr[p] is now at right place
    pi = partition(arr, low, high);

    // Before pi
    quickSort(arr, low, pi - 1);
    // After pi
    quickSort(arr, pi + 1, high);
  }
}
