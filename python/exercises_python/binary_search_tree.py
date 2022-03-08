# from typing import Any
# 難しいので繰り返し復習しよう！！ 220308

class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

# クラスで定義


class BinarySearchTree(object):
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: int) -> None:

        if self.root is None:
            self.root = Node(value)
            return

        def _insert(node: Node, value: int) -> Node:  # インナー関数の定義値を挿入する リカーシブル
            if node is None:
                return Node(value)

            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        _insert(self.root, value)

    def inorder(self) -> None:
        def _inorder(node: Node) -> Node:  # 1,3,5,6,7,10 の順に表示される
            if node is not None:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)

        _inorder(self.root)

    def search(self, value: int) -> bool:
        def _search(node: Node, value: int) -> bool:
            if node is None:
                return False

            if node.value == value:
                return True

            elif node.value > value:
                return _search(node.left, value)

            elif node.value < value:
                return _search(node.right, value)
        return _search(self.root, value)

    def min_value(node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def remove(self, value: int) -> None:
        def _remove(node: Node, value: int) -> Node:
            if node is None:
                return node
            if value < node.value:
                node.left = _remove(node.left, value)
            elif value > node.value:
                node.right = _remove(node.right, value)

            else:  # 値が一致した場合は削除
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                temp = self.min_value(node.right)
                node.value = temp.value
                node.right = _remove(node.right, temp.value)
            return node
        _remove(self.root, value)


if __name__ == '__main__':
    binary_tree = BinarySearchTree()
    binary_tree.insert(3)
    binary_tree.insert(6)
    binary_tree.insert(5)
    binary_tree.insert(7)
    binary_tree.insert(1)
    binary_tree.insert(10)
    binary_tree.insert(2)
    binary_tree.inorder()
    print("After Removed")
    binary_tree.remove(10)
    binary_tree.inorder()
    # root = None
    # root = insert(root, 3)
    # root = insert(root, 6)
    # root = insert(root, 5)
    # root = insert(root, 7)
    # root = insert(root, 1)
    # root = insert(root, 10)
    # inorder(root)
    # # print(search(root, 4))
    # root = remove(root, 6)
    # print("After Removed")
    # inorder(root)

# def insert(node: Node, value: int) -> Node:  # 値を挿入する リカーシブル
#     if node is None:
#         return Node(value)

#     if value < node.value:
#         node.left = insert(node.left, value)
#     else:
#         node.right = insert(node.right, value)
#     return node


# def inorder(node: Node) -> Node:  # 1,3,5,6,7,10 の順に表示される
#     if node is not None:
#         inorder(node.left)
#         print(node.value)
#         inorder(node.right)
    # Inorder Left Root Right  よく使われる探索順
    # Preorder Root Left Right
    # Postorder Left Right Root


# def search(node: Node, value: int) -> bool:
#     if node is None:
#         return False

#     if node.value == value:
#         return True

#     elif node.value > value:
#         return search(node.left, value)

#     elif node.value < value:
#         return search(node.right, value)


# def min_value(node: Node) -> Node:
#     current = node
#     while current.left is not None:
#         current = current.left
#     return current


# def remove(node: Node, value: int) -> Node:
#     if node is None:
#         return node
#     if value < node.value:
#         node.left = remove(node.left, value)
#     elif value > node.value:
#         node.right = remove(node.right, value)

#     else:  # 値が一致した場合は削除
#         if node.left is None:
#             return node.right
#         elif node.right is None:
#             return node.left

#         temp = min_value(node.right)
#         node.value = temp.value
#         node.right = remove(node.right, temp.value)
#     return node
