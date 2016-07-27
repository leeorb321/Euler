public class Problem005 {

    public static void main( String[] args ) {
        int result = divisibleTo(20);
        System.out.println(result);
    }

    private static boolean isDivisibleTo(int num, int max) {
        for (int i = max; i > 1; i--) {
            if (num % i != 0) {
                return false;
            }
        }
        return true;
    }

    private static int divisibleTo(int num) {
        if (num <= 1) {
            return num;
        }

        int step = divisibleTo(num - 1);
        int currentAttempt = 0;
        boolean complete = false;

        while (!complete) {
            currentAttempt += step;
            complete = isDivisibleTo(currentAttempt, num);
        }

        return currentAttempt;
    }
}
