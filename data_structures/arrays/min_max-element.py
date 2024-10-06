"""
Author - Seema Kumari Patel - 2024

Retrieves minimum and maximum valued number from an array.
There are two ways to retrieve value(s):

1. Approach #01 -Linear Search.
Initialize values of min and max as minimum and maximum of the first two elements respectively.
Starting from 3rd, compare each element with max and min, and change max and min accordingly.

2. Approach #02 - First sort the array in ascending order.
Once the array is sorted, the first element of the array will be the minimum element and the last element of the array will be the maximum element.

Here is the code for second approach
"""

import java.io.*;
import java.util.*;


'''To get the values to min / max respectively'''
class Pair {
    public int min;
    public int max;
}

'''To sort the array in ascending order'''
class Main {
    static Pair getMinMax(int arr[], int n) {
        Pair minmax = new Pair();
        Arrays.sort(arr);
        minmax.min = arr[0];
        minmax.max = arr[n - 1];
        return minmax;
    }

'''To get the array elements'''
    public static void main(String[] args) {
        int arr[] = { 1000, 11, 445, 1, 330, 3000 };
        int arr_size = arr.length;
        Pair minmax = getMinMax(arr, arr_size);
        System.out.println("Minimum element is " + minmax.min);
        System.out.println("Maximum element is " + minmax.max);
    }
}
