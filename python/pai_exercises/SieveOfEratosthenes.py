# coding: UTF-8
import math
# エラトステネスの篩 指定された整数以下の全ての素数を発見するための単純なアルゴリズム
# 1. X が素数のとき is_prime[X] が true となる配列 is_prime を用意し、
# is_prime[0], is_prime[1] を false, それ以外を true で初期化する。
# 2. 整数 i を 2 から順に N まで動かしながら次の操作を行う。
# 「is_prime[i] が true である場合、 is_prime[2×i], is_prime[3×i], ..., is_prime[k×i] を全て false にする（ただし k×i <= N ）

N = int(input())
is_prime = True

if N == 1:
    is_prime = False

# print(math.sqrt(N))
n = math.ceil(math.sqrt(N))
# print(n)
for i in range(2, n):
    if N % i == 0:
        # print(i)
        is_prime = False
        break

if is_prime == True:
    print("YES")
else:
    print("NO")
