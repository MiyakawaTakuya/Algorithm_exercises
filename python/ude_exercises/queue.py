from typing import Any
# キューの理解をしよう  入った順番に出てくる
# pythonの場合は ライブラリで以下のものを使って実装することもできる
from collections import deque


class Queue(object):

    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, data: Any) -> None:
        self.queue.append(data)

    def dequeue(self) -> Any:  # なんでもいい string int
        if self.queue:  # もしstackがあれば 一番後ろのものを返す
            return self.queue.pop(0)  # 0とインデックスを指定してやることで先頭から取り出す処理になる


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue("あ")
    q.enqueue(100)
    print(q.queue)
    q.dequeue()
    print(q.queue)
    q.dequeue()
    q.dequeue()
    print(q.queue)
