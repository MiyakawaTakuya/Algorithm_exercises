# coding: UTF-8
# Python3では、整数型(int) と長整数型(long)は統合されて、すべて整数(int)となりました。
# sqrt https://techacademy.jp/magazine/20603
# for https://udemy.benesse.co.jp/development/python-work/python-for.html
# math.floor ceil https://note.nkmk.me/python-math-floor-ceil-int/
import math
# import os
# folder = os.getcwd()
# print(folder) #/Users/miyagawatakuya/G's Task/Algorithm/python/pai_exercises

# # if __name__ == '__main__':
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


# int main() {
#   long long int n
#   cin >> n
#   bool is_prime = true

#   if (n == 1) {
#       is_prime = false
#   }

#   for (long long int i=2
#        i * i <= n
#        i++) {
#       if (n % i == 0) {
#           is_prime = false
#       }
#   }

#   if (is_prime) {
#       cout << "YES" << endl
#   } else {
#       cout << "NO" << endl
#   }
# }
