# 左右対称のペアを見つけてその値を返すアルゴリズム
"""
Symmetric
Input  [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
Output [(5, 3), (7, 4)]
"""

from typing import List, Iterator, Tuple


def find_pair(pairs: List[Tuple[int, int]]) -> Iterator[Tuple[int, int]]:
    cache = {}  # ハッシュテーブルを用意して、順次追加していく方針
    for pair in pairs:
        first, second = pair[0], pair[1]
        value = cache.get(second)  # secondの値で該当するキーがないかcacheの中を探す
        if not value:
            cache[first] = second
        elif value == first:
            yield pair  # pairを戻り値として返して、処理を一旦停止する


if __name__ == '__main__':
    l = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
    for r in find_pair(l):
        print(r)
# (5, 3)
# (7, 4)
