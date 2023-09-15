/*
 * Insertion sort
 * Time complexity: O(n^2)
 * Space complexity: O(1)
 */

public class InsertionSort {
    public static void main(String[] args) {
        int[] arr = { 12, 11, 13, 5, 6 };

        sort(arr);

        System.out.println("Sorted array: ");
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }

    public static void sort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            for (int num : arr) {
                System.out.print(num + " ");
            }
            System.out.println();

            int number = arr[i];
            int j = i - 1; // previous index

            //
            while (j >= 0 && arr[j] > number) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = number;
        }
    }
}
