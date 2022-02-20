//220220 再帰関数プログラム
//トリボナッチ数とは、次のように定義される数列です。
// T(0) = 0
// T(1) = 0
// T(2) = 1
// T(n) = T(n - 1) + T(n - 2) + T(n - 3)
// たとえば、4番目のトリボナッチ数は、次のように計算します。
// T(4) = T(3) + T(2) + T(1) = 1 + 1 + 0 = 2

// public class Tribonacci {
//     public static void main(String[] args) throws Exception {
//         int number = 50;
//         for (int i = 0; i <= number; i++) {
//             System.out.println(i + ": " + tribonacci(i));
//         }
//     }

//     public static long tribonacci(int num) {
//         // トリボナッチ数の最初の3項(0, 0, 1)を用いて，再起呼び出し
//         return tri2(0, 0, 1, num);
//     }

//     public static long tri2(long a, long b, long c, long d) {
//         if (d <= 1) {
//             return 0;
//         }
//         // 再起の深さがd
//         if (d == 2) {
//             return c;
//         }
//         // 再起呼び出し
//         return tri2(b, c, a + b + c, d - 1);
//     }
// }

//////模範回答
// トリボナッチ数
// 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149
// 再帰を用いて作成
public class Tribonacci {
    public static void main(String[] args) throws Exception {
        int number = 50;
        for (int i = 0; i <= number; i++) {
            System.out.println(i + ": " + tribonacci(i));
        }
    }

    public static long tribonacci(int num) {
        // トリボナッチ数の最初の3項(0, 0, 1)を用いて，再起呼び出し
        return tri2(0, 0, 1, num);
    }

    public static long tri2(long a, long b, long c, long d) {
        // 再起の深さがd
        if (d < 2) {
            return a;
            // return c;
        }
        // 再起呼び出し
        return tri2(a + b + c, a, b, d - 1);
        // return tri2(b, c, a + b + c, d - 1);
    }
}

// 正解出力
// 0: 0
// 1: 0
// 2: 1
// 3: 1
// 4: 2
// 5: 4
// 6: 7
// 7: 13
// 8: 24
// 9: 44
// 10: 81
// 11: 149
// 12: 274
// 13: 504
// 14: 927
// 15: 1705
// 16: 3136
// 17: 5768
// 18: 10609
// 19: 19513
// 20: 35890
