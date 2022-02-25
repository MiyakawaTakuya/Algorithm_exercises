// import java.util.*;

public class Fibonacci_Binet_Formula {
    public static void main(String[] args) throws Exception {
        int number = 50;
        for (int i = 0; i <= number; i++) {
            System.out.println(i + ":" + fibonacci(i));
        }
    }

    public static long fibonacci(int num) {
        return Math.round((Math.pow((1 + Math.sqrt(5)) / 2, num)
                - Math.pow((1 - Math.sqrt(5)) / 2, num)) / Math.sqrt(5));
    }
}
