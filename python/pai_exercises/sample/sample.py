# coding: UTF-8
# 入力
#input_line = input()
# print(input_line)

# for i in range(10):
#    input_line = input()
#    print(input_line)

# line, line2 = input().split()
# print(line)
# print(line2)

#input_line = input().split()
# print(input_line[0])
# print(input_line[1])

# line = input().split()
# for _ in range(3):
#     print(line[_])

# lines = input().split()
# [print(i) for i in lines]  #リスト内包表記

# for _ in range(100):
#     line = input()
#     print(line)

# N = int(input())
# for _ in range(N):
#     line = input()
#     print(line)

# N = int(input())
# for _ in range(N):
#     line = input()
#     if _ == 7:
#         print(line)

# a,b,c = map(int, input().split())
# print(a)
# print(b)
# print(c)

# lists = map(int, input().split())   #複数の値をタプルで受け取ってリストにする
# [print(i) for i in lists]


# 自作クラス
class Pack:
    machines = []  # クラス変数
    # インスタンス化する時に __init__ が、自動的に呼び出される。

    def __init__(self, num, i):  # 初期化
        # 第一引数 self には名前のないオブジェクトが自動的に代入されている。
        self.packageNum = num
        self.amari = 10 % num
        self.machineNo = i + 1
        # selfはreturn不要
        # 関数とは違い  return 文を使わなくても  自動的に self が返される。


M, N = map(int, input().split())
machines_list = [Pack(int(input()), i) for i in range(M)]
