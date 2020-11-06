public class J1198317
{
    public static void main(String[] args) {
        int[] arr = {0, 2, 1, 1, 9, 1};
        int sum = 0;
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            count++;
            sum += arr[i];
            if (sum >= 4) break;
        }
        if (sum == 4) System.out.println("Found: " + count);
        else  System.out.println("Not found: " + count);
    }
}

