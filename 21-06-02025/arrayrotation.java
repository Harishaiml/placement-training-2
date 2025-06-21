public class ArrayRotation {
    public static void rotateArray(int[] arr, int k) {
        int n = arr.length;
        k = k % n; // Handle rotations larger than array size
        int[] temp = new int[k];
        for (int i = 0; i < k; i++) {
            temp[i] = arr[i];
        }
        for (int i = k; i < n; i++) {
            arr[i - k] = arr[i];
        }
        for (int i = 0; i < k; i++) {
            arr[n - k + i] = temp[i];
        }
    }

    public static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int k = 2;
        System.out.print("Original array: ");
        printArray(arr);
        rotateArray(arr, k);
        System.out.print("Rotated array: ");
        printArray(arr);
    }
}
