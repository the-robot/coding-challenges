package algods;

import algods.heaps.MaxHeap;
import algods.heaps.MinHeap;

/*
 * Heap sort
 * Time complexity: O(n log n)
 * Space complexity: O(1) because it is in-place sorting algorithm.
 */

public class HeapSort {
    public static void heapSortMax(int[] arr) {
        int n = arr.length;

        // Build a max heap
        MaxHeap maxHeap = new MaxHeap(n);
        for (int i = 0; i < n; i++) {
            maxHeap.insert(arr[i]);
        }

        // Extract elements in ascending order
        for (int i = n - 1; i >= 0; i--) {
            arr[i] = maxHeap.extractMax();
        }
    }

    public static void heapSortMin(int[] arr) {
        int n = arr.length;

        // Build a min heap
        MinHeap minHeap = new MinHeap(n);
        for (int i = 0; i < n; i++) {
            minHeap.insert(arr[i]);
        }

        // Extract elements in ascending order
        for (int i = 0; i < n; i++) {
            arr[i] = minHeap.extractMin();
        }
    }

    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6, 7};
        
        System.out.println("Original array:");
        for (int num : arr) {
            System.out.print(num + " ");
        }

        heapSortMax(arr); // Use max heap for ascending order

        System.out.println("\nSorted array using MaxHeapSort:");
        for (int num : arr) {
            System.out.print(num + " ");
        }

        int[] arr2 = {12, 11, 13, 5, 6, 7};

        heapSortMin(arr2); // Use min heap for ascending order

        System.out.println("\nSorted array using MinHeapSort:");
        for (int num : arr2) {
            System.out.print(num + " ");
        }
    }
}
