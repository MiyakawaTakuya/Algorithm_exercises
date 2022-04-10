# 371. Sum of Two Integers
# Given two integers a and b, return the sum of the two integers without using the operators + and -.
# pythonでバイナリ関数を使う https://www.delftstack.com/ja/howto/python/python-int-to-binary/
# Pythonのビット演算子 https://note.nkmk.me/python-bit-operation/

class Solution:
    # def getSum(self, a: int, b: int) -> int:
    #     temp_a = format(a, "b")
    #     temp_b = format(b, "b")
    #     print(temp_a)
    #     print(temp_b)
    #     return 0


# Approach 1: Bit Manipulation: Easy and Language-Independent
# Algorithm
# Simplify problem down to two cases: sum or subtraction of two positive integers: x \pm yx±y, where x > yx > y. Save down the sign of the result.
# If one has to compute the sum:
# While carry is nonzero: y != 0:
# Current answer without carry is XOR of x and y: answer = x ^ y.
# Current carry is left-shifted AND of x and y: carry = (x & y) << 1.
# Job is done, prepare the next loop: x = answer, y = carry.
# Return x * sign.
# If one has to compute the difference:
# While borrow is nonzero: y != 0:
# Current answer without borrow is XOR of x and y: answer = x ^ y.
# Current borrow is left-shifted AND of NOT x and y: borrow = ((~x) & y) << 1.
# Job is done, prepare the next loop: x = answer, y = borrow.
# Return x * sign.

    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure that abs(a) >= abs(b)
        if x < y:
            return self.getSum(b, a)
        # abs(a) >= abs(b) -->
        # a determines the sign
        sign = 1 if a > 0 else -1
        if a * b >= 0:
            # sum of two positive integers x + y
            # where x > y
            while y:
                answer = x ^ y  #0001 ^ 0010  = 0011 (3)
                # 論理積（AND）: &演算子  ビットシフト演算子<<, >>による、左ビットシフト、右ビットシフト
                carry = (x & y) << 1 #左シフトを入れる理由がよくわからん...いずれにせよ0のままな気がする
                x, y = answer, carry  #0011, 0110
        else:
            # difference of two integers x - y
            # where x > y
            while y:
                answer = x ^ y
                borrow = ((~x) & y) << 1
                x, y = answer, borrow

        return x * sign


solution = Solution()
a = 1
b = 2
print(solution.getSum(a, b))

# Input: a = 1, b = 2
# Output: 3
# -1000 <= a, b <= 1000
