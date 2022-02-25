//プログラムは解法が一つじゃない。複数の方法でプログラムを作れるようになるべし。

// import java.util.*;

public class FizzBuzz {
    public static void main(String[] args) throws Exception {
        String output;
        for (int i = 1; i <= 30; i++) {
            output = "";
            if (i % 3 == 0) {
                output = "Fizz";
            }
            if (i % 5 == 0) {
                output += "Buzz";
            }
            output = String.valueOf(i) + ":" + output;
            System.out.println(output);
        }
    }

    // public static void main(String[] args) throws Exception {
    // String output;
    // for (int i = 1; i <= 100; i++) {
    // if (i % 3 == 0 && i % 5 == 0) { // 3の倍数でかつ5の倍数のとき
    // output = i + ": HogeFuga"; // ここを修正
    // } else if (i % 3 == 0) { // 3の倍数のとき
    // output = i + ": Hoge"; // ここを修正
    // } else if (i % 5 == 0) { // 5の倍数のとき
    // output = i + ": Fuga"; // ここを修正
    // } else { // 上のすべての条件を満たさなかったとき
    // output = String.valueOf(i);
    // }
    // System.out.println(output);
    // }

    // }

}
