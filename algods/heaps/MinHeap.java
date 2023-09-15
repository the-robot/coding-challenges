package algods.heaps;

public class MinHeap {
    private int[] heap;
    private int size;
    private int capacity;

    public MinHeap(int capacity) {
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
        while (index > 0 && heap[index] < heap[parentIndex]) {
            swap(index, parentIndex);
            index = parentIndex;
            parentIndex = getParentIndex(index);
        }
    }

    private void heapifyDown(int index) {
        int leftChildIndex = getLeftChildIndex(index);
        int rightChildIndex = getRightChildIndex(index);
        int smallest = index;

        if (leftChildIndex < size && heap[leftChildIndex] < heap[smallest]) {
            smallest = leftChildIndex;
        }

        if (rightChildIndex < size && heap[rightChildIndex] < heap[smallest]) {
            smallest = rightChildIndex;
        }

        if (index != smallest) {
            swap(index, smallest);
            heapifyDown(smallest);
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

    public int extractMin() {
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

    public int getMin() {
        if (size <= 0) {
            System.out.println("Heap is empty.");
            return -1;
        }

        return heap[0];
    }

    public static void main(String[] args) {
        MinHeap minHeap = new MinHeap(10);
        minHeap.insert(4);
        minHeap.insert(9);
        minHeap.insert(2);
        minHeap.insert(7);
        minHeap.insert(5);

        System.out.println("Min element: " + minHeap.getMin());

        System.out.println("Extracting min elements:");
        while (minHeap.size > 0) {
            System.out.println(minHeap.extractMin());
        }
    }
}