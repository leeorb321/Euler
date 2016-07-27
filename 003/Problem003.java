public class Problem003 {
    public static void main( String[] args ) {
        int result = largestPrimeFactor(600851475143L);
        System.out.println(result);

    }

    private static int largestPrimeFactor(long n) {
        int largest = 1;
        int temp = 0;
        if (n % 2 == 0) {
            largest = 2;
            n /= 2;
        }
        long p = n;
        int current = 3;
        while (n != 1 && current <= Math.sqrt(p)) {
            while (n % current == 0) {
                largest = current;
                n /= current;
            }
            current += 2;
        }
        return largest;
    }
}
