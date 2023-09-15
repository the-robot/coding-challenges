package algods.heaps;

public class MaxHeap {
    private int[] heap;
    private int size;
    private int capacity;

    public MaxHeap(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.heap = new int[capacity];
    }

    private int getParentIndex(int index) {
        return (index - 1) / 2;
    }

    private int getLeftChildIndex(int index) {
        return 2 * index + 1;
    }

    private int getRightChildIndex(int index) {
        return 2 * index + 2;
    }

    private void swap(int a, int b) {
        int temp = heap[a];
        heap[a] = heap[b];
        heap[b] = temp;
    }

    private void heapifyUp(int index) {
        int parentIndex = getParentIndex(index);
        while (index > 0 && heap[index] > heap[parentIndex]) {
            swap(index, parentIndex);
            index = parentIndex;
            parentIndex = getParentIndex(index);
        }
    }

    private void heapifyDown(int index) {
        int leftChildIndex = getLeftChildIndex(index);
        int rightChildIndex = getRightChildIndex(index);
        int largest = index;

        if (leftChildIndex < size && heap[leftChildIndex] > heap[largest]) {
            largest = leftChildIndex;
        }

        if (rightChildIndex < size && heap[rightChildIndex] > heap[largest]) {
            largest = rightChildIndex;
        }

        if (index != largest) {
            swap(index, largest);
            heapifyDown(largest);
        }
    }

    public void insert(int value) {
        if (size == capacity) {
            System.out.println("Heap is full. Cannot insert.");
            return;
        }

        size++;
        heap[size - 1] = value;
        heapifyUp(size - 1);
    }

    public int extractMax() {
        if (size <= 0) {
            System.out.println("Heap is empty.");
            return -1;
        }

        if (size == 1) {
            size--;
            return heap[0];
        }

        int root = heap[0];
        heap[0] = heap[size - 1];
        size--;
        heapifyDown(0);

        return root;
    }

    public int getMax() {
        if (size <= 0) {
            System.out.println("Heap is empty.");
            return -1;
        }

        return heap[0];
    }

    public static void main(String[] args) {
        MaxHeap maxHeap = new MaxHeap(10);
        maxHeap.insert(4);
        maxHeap.insert(9);
        maxHeap.insert(2);
        maxHeap.insert(7);
        maxHeap.insert(5);

        System.out.println("Max element: " + maxHeap.getMax());

        System.out.println("Extracting max elements:");
        while (maxHeap.size > 0) {
            System.out.println(maxHeap.extractMax());
        }
    }
}
