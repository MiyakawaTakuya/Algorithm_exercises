from collections import deque


def reverse(queue: deque) -> deque:
    new_queue = deque()
    while queue:  # queueがある間
        # print(queue.pop())
        new_queue.append(queue.pop())  # 最後に履いている値を取り出して、newqueueに追加する
    # 入れ替わってできたnewqueueをqueueに順番に追加して行って、最後に返り値として返す
    [queue.append(d) for d in new_queue]
    # return new_queue


if __name__ == '__main__':
    q = deque()
    q.append(1)
    q.append(10)
    q.append(100)
    print(q)
    # q = reverse(q)
    reverse(q)
    print(q)
