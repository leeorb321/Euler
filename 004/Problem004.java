public class Problem004 {

    public static void main( String[] args ) {
        int result = largestPalindromeProduct(999,999);
        System.out.println(result);
    }

    private static int largestPalindromeProduct(int a, int b) {
        int largest = 0;
        String current;
        for (int i = 0; i < a; i++) {
            for (int j = i; j < b; j++) {
                current = String.valueOf(i*j);
                if (isPalindrome(current) && i*j > largest) {
                    largest = i*j;
                }
            }
        }
        return largest;
    }

    private static boolean isPalindrome(String s) {
        for (int i = 0; i < s.length()/2; i++) {
            if (s.charAt(i) != s.charAt(s.length() - i - 1)) {
                return false;
            }
        }
        return true;
    }
}
