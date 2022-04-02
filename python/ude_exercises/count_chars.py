# Input: 'This is a pen. This is an apple. Applepen.'
# Output: ('p', 6)
from collections import Counter
import operator
from typing import Tuple


def count_chars_v1(strings: str) -> Tuple[str, int]:    # ディクショナリーを使わない方法
    strings = strings.lower()  # 小文字にするメソッド
    # l = []
    # for char in strings:
    #     if not char.isspace():  #スペースでなければカウントする
    #         l.append((char, strings.count(char)))
    l = [(c, strings.count(c)) for c in strings if not c.isspace()]
    # return l
    return max(l, key=operator.itemgetter(1))
    # #operator.itemgetter(1) は連想配列の１番目(intの部分)に着目する
    # https://techacademy.jp/magazine/26352  itemgetter()の利用方法
    # itemgetterは[]に対応する関数であり、イテラブル(リスト,文字列などfor文のinに書き込めるオブジェクト)から任意の要素を取得する呼び出し可能なオブジェクトを作成します。

    # return max(l, key=l.get)  はd = {'a': 100, 'b': 20, 'c': 50, 'd': 100, 'e': 80} のような辞書だったら使えるみたい
    # https://note.nkmk.me/python-dict-value-max-min/  Pythonで辞書の値の最大値・最小値とそのキーを取得


def count_chars_v2(strings: str) -> Tuple[str, int]:    # ディクショナリーを使う方法
    strings = strings.lower()
    d = {}  # {2,2}と宣言してしまうと集合になる
    # print(d,type(d))
    # d=dict()
    for char in strings:
        if not char.isspace():  # スペースでなければカウントする
            d[char] = d.get(char, 0)+1
    # print(d)
    #{'t': 2, 'h': 2, 'i': 4, 's': 4, 'a': 4, 'p': 6, 'e': 4, 'n': 3, '.': 3, 'l': 2}
    max_key = max(d, key=d.get)
    return max_key, d[max_key]


# ディクショナリーを使って、カウンタークラスを使う方法
def count_chars_v3(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    d = Counter()  # デフォルトでキーのバリューに0が入っている
    for char in strings:
        if not char.isspace():  # スペースでなければカウントする
            d[char] += 1
    max_key = max(d, key=d.get)
    return max_key, d[max_key]


if __name__ == '__main__':
    s = 'This is a pen. This is an apple. Applepen.'
    print(count_chars_v3(s))
