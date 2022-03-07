from typing import Any


class Stack(object):

    def __init__(self) -> None:
        self.stack = []

    def push(self, data) -> None:
        self.stack.append(data)

    def pop(self) -> Any:  # なんでもいい string int
        if self.stack:  # もしstackがあれば 一番後ろのものを返す
            return self.stack.pop()


if __name__ == '__main__':
    stack = Stack()
    print(stack.stack)
    stack.push(1)
    print(stack.stack)
    stack.push(5)
    print(stack.stack)  # [1, 5]
    print(stack.pop())  # 5
    print(stack.stack)  # [1]
