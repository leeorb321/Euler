public class Problem002 {
    public static void main( String[] args ) {
        int sum = fibo(4000000);
        System.out.println(sum);
    }

    static int fibo(int n) {
        int sum = 0;
        int a = 0;
        int b = 1;
        int temp = 0;
        while (b < n) {
            temp = a;
            a = b;
            b += temp;
            if (b % 2 == 0){
                sum += b;
            }
        }
        return sum;
    }
}
