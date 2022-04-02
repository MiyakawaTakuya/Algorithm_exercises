X, Y, Z = map(int, input().split())
vertical_X = []
vertical_part = ['.' for _ in range(Y)]  # .で充填しておく
i = 0
for z in range(Z):
    for x in range(X):
        inp = input()
        for cha in inp:
            if cha == '#':
                vertical_part[i] = '#'
            i += 1
        i = 0
    _ = input()  # ここで--を掬い取る
    vertical_X.insert(0, ''.join(vertical_part))  # 回答となる配列の先頭に、配列をjoinしていく
    vertical_part = ['.' for _ in range(Y)]  # .で充填してリセットかける
# 出力
for v in vertical_X:
    print(v)
